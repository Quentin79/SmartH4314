#!/usr/bin/python

import sys
import json
import requests
import grequests
import time

import psycopg2


##################
## Class Engine ##
##################

class FeedTheDBHierarchie:

	# Core of the class
	def run(self):
		# connect postgres
		try:
			connPostgres = psycopg2.connect("dbname='postgres' user='postgres' host='172.17.0.4' password='admin'")
		except:
			print "Error unable to connect postgres"
			return

		cur = connPostgres.cursor()
		cur.execute("SELECT nom FROM public.\"DataGL4\" WHERE \"hierarchieSet\" = 'false' ORDER BY index LIMIT 5")
		rows = cur.fetchall()

		print "result:\n"
		for row in rows:
			print "   ", row[0]
		
		self.requetsBlumix(rows)
		
		# request alchemy
	def requetsBlumix (self, noms):
		for nom in noms :
			parameters = {
			"text": nom,
			"features": {
			"concepts": {
			"limit": 1
			}
			},
			"clean": "true",
			"fallback_to_raw": "true",
			"return_analyzed_text": "false",
			"language": "fr"
			}		  
			r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api', params=parameters, auth=('dc479c4a-de18-4be3-9095-8bb3fc537b58','DuxBm28zBvaB'))
			print r.json()
		##############
##   MAIN   ##
##############

def main():
	f = FeedTheDBHierarchie()
	f.run()


if __name__ == "__main__":
    main()
