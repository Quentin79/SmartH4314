import requests
import pandas as pd
from pg import DB
from sqlalchemy import create_engine
import json

fic = open("MaSauvegardeFrom4998.txt","r")
contenu = fic.read()
dico = eval (contenu)
df = pd.DataFrame(dico, index=range(4999,4999+43 ))
#df = pd.read_json('MaSauvegardeFrom30.json')
engine = create_engine('postgresql://postgres:admin@172.17.0.4:5432/postgres')
df.to_sql('GLOntology', engine, if_exists = 'append')
