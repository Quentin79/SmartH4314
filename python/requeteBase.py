#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from pg import DB
from modifString import modifierString
import json

def fetchDataAll (db, likes):
	query = "SELECT nom,adresse FROM public.\"DataGL4\" WHERE "
	for like in likes:
		like = modifierString(like)
		query += "nom_normalize like '%"+like+"%' or "
	query +='1=2'
	q=db.query(query)
	#q = db.query("SELECT nom,adresse FROM public.\"DataGL4\" WHERE nom_normalize like '%"+like+"%'")
	#q = db.query("SELECT nom,adresse FROM public.\"DataGL4\" WHERE nom_normalize like '%tetedor%'")
	#print(query)
	#print('\r\n');
	#print(json.dumps(q.dictresult()))

	return json.dumps(q.dictresult())


def fetchDataSingle (db, like):
	likeNorma = modifierString(like)
	query = "SELECT nom,adresse FROM public.\"DataGL4\" WHERE nom_normalize like '%"+likeNorma+"%' "
	q=db.query(query)

	return json.dumps(q.dictresult())

#db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
#listLike = ['Tête d\'or', 'le patineur']
#fetchData(db,listLike)
