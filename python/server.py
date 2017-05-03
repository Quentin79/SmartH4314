#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from FacebookAPI import FacebookAPI
from requeteBase import fetchData
from pg import DB
from flask import request
from flask import Response
import requests
import json
import psycopg2

app = Flask(__name__)

@app.route('/engine', methods=['GET', 'POST'])
def main(): #enlever token
	#token = 'EAACEdEose0cBADbHU92C4fP13NnLV9ZB7x7qqRiuF5W3fw6ZBZCFZBlx3QhuhgObNiGAJHL36pw8ujwLKkJAUwEIFJQ4zZAilMw3skQ5wOQLP3vk1ZBDgTDM8pbsNeMClB4Fla1EH6P3AiEwlIANC34SyZCSWGUTdsSZBaEWPyyB9K5ZAVDOZAFpOGetpKZCKhhIA8ZD'
	token = request.args.get('token')
	#return token
	db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
	myFacebook = FacebookAPI(access_token = token)
	likes = myFacebook.getNamesFromFacebookLikes()
	
	#return json.dumps(likes)
	#likes=['Tête dor']
	json_response=fetchData(db,likes)
	#print ('\r\n')
	#print (json_response)
	reponse = Response("")
	reponse.headers['Access-Control-Allow-Origin'] = '*'
	reponse.data = json_response
	reponse.mimetype = "json"
	return reponse

@app.route('/reconiveau2', methods=['GET', 'POST'])
def RecoNiveau2EntryPoint():
	
	try:
		token = request.args.get('token')
	except:
		return '{"error":"Need a token access"}'
	
	if token is None :
		return '{"error":"Need a token access"}'
	myFacebook = FacebookAPI(access_token = token)

	pagesDescription = myFacebook.get_pages_from_ids()
	
	reponse = Response("")
	reponse.headers['Access-Control-Allow-Origin'] = '*'
	reponse.data = json.dumps(level2Recommandations(pagesDescription))
	reponse.mimetype = "json"
	return reponse
		

def level2Recommandations(pagesDescription):
	ontologieliste = []
	recommandation = {}
	 
	
	try:
		conn = psycopg2.connect("dbname='postgres' user='postgres' host='172.17.0.4' password='admin'")
	except:
		print "I am unable to connect to the database"

	pagesDescription = pagesDescription[0]
	# pour chaque likes
	for key, val in pagesDescription.items() :
		# on construit une requête dont le text est le like et la description
		parameters = {
		"version" : "2017-02-27",
		"text": val["name"]+" "+val["description"],
		"features": {"categories": {"limit" : 1}}}

		# envoie de la requete à watson
		r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze', params=parameters, auth=('dc479c4a-de18-4be3-9095-8bb3fc537b58','DuxBm28zBvaB'))

		jsonObject = r.json()
		listCtgr = []

		if jsonObject['categories'] :
			categories = jsonObject['categories'][0]['label']
			listCtgr = categories.split('/')
			listCtgr.pop(0)

			listCtgr.extend(['']*(5-len(listCtgr)))
			
			nom = val["name"]
			# on récupère les cétégories
			param = {
			'nom': nom,
			'label0' : listCtgr[0],
			'label1' : listCtgr[1],
			'label2' : listCtgr[2],
			'label3' : listCtgr[3],
			'label4' : listCtgr[4]
			}

			# on ajoute les params courants à la liste d'ontologie
			# ontologieliste.append(param)

			# requête postgres 
			cur = conn.cursor()

			cur.execute("WITH reco as(Select \"DataGL4\".id, nom, adresse, (0+0.2*(\"l1\"= '"+listCtgr[0]+"')::int+0.4*(\"l2\"= '"+listCtgr[1]+"')::int+0.6*(\"l3\"= '"+listCtgr[2]+"')::int+0.8*(\"l4\"= '"+listCtgr[3]+"')::int+1*(\"l5\"= '"+listCtgr[4]+"')::int) AS ressemblanceCoefficient from public.\"hierarchie\", public.\"DataGL4\" Where \"hierarchie\".id=\"DataGL4\".index LIMIT 2)SELECT * FROM reco WHERE ressemblanceCoefficient > 0;")

			rows = cur.fetchall()

			recommandation[nom]=[]
			for row in rows:
				recommandation[nom].append({"nom":row[1], "address":row[2], "coefficient": float(row[3])})
	return recommandation



	




#main('EAACEdEose0cBADbHU92C4fP13NnLV9ZB7x7qqRiuF5W3fw6ZBZCFZBlx3QhuhgObNiGAJHL36pw8ujwLKkJAUwEIFJQ4zZAilMw3skQ5wOQLP3vk1ZBDgTDM8pbsNeMClB4Fla1EH6P3AiEwlIANC34SyZCSWGUTdsSZBaEWPyyB9K5ZAVDOZAFpOGetpKZCKhhIA8ZD')
