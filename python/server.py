#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from FacebookAPI import FacebookAPI
from requeteBase import fetchData
from pg import DB

app = Flask(__name__)

@app.route('/engine', methods=['GET', 'POST'])
def main():
	#token = 'EAACEdEose0cBADbHU92C4fP13NnLV9ZB7x7qqRiuF5W3fw6ZBZCFZBlx3QhuhgObNiGAJHL36pw8ujwLKkJAUwEIFJQ4zZAilMw3skQ5wOQLP3vk1ZBDgTDM8pbsNeMClB4Fla1EH6P3AiEwlIANC34SyZCSWGUTdsSZBaEWPyyB9K5ZAVDOZAFpOGetpKZCKhhIA8ZD'
	token = request.args.get('token')
	db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
	myFacebook = FacebookAPI(access_token = token)
	likes = myFacebook.getNamesFromFacebookLikes()
	#print (likes)
	#likes=['Tête dor']
	json_response=fetchData(db,likes)
	#print ('\r\n')
	#print (json_response)
	return json_response


@app.route('/test', methods=['GET', 'POST'])
def main2():
	return "hello world"




#main('EAACEdEose0cBADbHU92C4fP13NnLV9ZB7x7qqRiuF5W3fw6ZBZCFZBlx3QhuhgObNiGAJHL36pw8ujwLKkJAUwEIFJQ4zZAilMw3skQ5wOQLP3vk1ZBDgTDM8pbsNeMClB4Fla1EH6P3AiEwlIANC34SyZCSWGUTdsSZBaEWPyyB9K5ZAVDOZAFpOGetpKZCKhhIA8ZD')
