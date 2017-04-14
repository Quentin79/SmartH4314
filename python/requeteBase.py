#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from pg import DB
from modifString import modifierString
import json

def fetchData (db, like):
	like = modifierString(like)
	q = db.query("SELECT nom,adresse FROM public.\"DataGL4\" WHERE nom_normalize like '%"+like+"%'")
	print(q.dictresult())
	print('\r\n');
	print(json.dumps(q.dictresult()))
	return q.dictresult()


fetchData(db,'Tête d\'or')
