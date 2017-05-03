#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from FacebookAPI import FacebookAPI
from requeteBase import fetchDataAll
from requeteBase import fetchDataSingle
from pg import DB
from flask import request
from flask import Response
import json

app = Flask(__name__)

@app.route('/engine', methods=['GET', 'POST'])
def main(): #enlever token
	#token = 'EAACEdEose0cBADbHU92C4fP13NnLV9ZB7x7qqRiuF5W3fw6ZBZCFZBlx3QhuhgObNiGAJHL36pw8ujwLKkJAUwEIFJQ4zZAilMw3skQ5wOQLP3vk1ZBDgTDM8pbsNeMClB4Fla1EH6P3AiEwlIANC34SyZCSWGUTdsSZBaEWPyyB9K5ZAVDOZAFpOGetpKZCKhhIA8ZD'
	token = request.args.get('token')
	#return token
	db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
	myFacebook = FacebookAPI(access_token = token)
	likes = myFacebook.getNamesFromFacebookLikes()

	dict_reponse = {}
	for like in likes :
		like = like.replace('"', '') #fait planter le front sinon
		like = like.replace('\'', '')  #fait planter le front sinon
		rep = fetchDataSingle(db,like)
	#	return json.dumps(rep)
		dict_reponse[like]=rep



	reponse = Response("")
	reponse.headers['Access-Control-Allow-Origin'] = '*'
	reponse.data = json.dumps(dict_reponse)
	reponse.mimetype = "json"
	return reponse


@app.route('/test', methods=['GET', 'POST'])
def main2():
	db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
	result = getNoms(db)
	return json.dumps(result) + str(len(result))
	
	
	
	

def getNoms (db) :
	return "hello world"


print("bonjour") 


#main('EAACEdEose0cBADbHU92C4fP13NnLV9ZB7x7qqRiuF5W3fw6ZBZCFZBlx3QhuhgObNiGAJHL36pw8ujwLKkJAUwEIFJQ4zZAilMw3skQ5wOQLP3vk1ZBDgTDM8pbsNeMClB4Fla1EH6P3AiEwlIANC34SyZCSWGUTdsSZBaEWPyyB9K5ZAVDOZAFpOGetpKZCKhhIA8ZD')
