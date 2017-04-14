from collections import namedtuple
import pandas as pd
import requests

print("Traitement données du grand Lyon \r\n")

##On recupere le fichier json
r = requests.get('https://download.data.grandlyon.com/ws/rdata/sit_sitra.sittourisme/all.json')
text_obj = r.json()

##Déf d'un tuple comprenant tous les champs d'une entrée du json
Evenement = namedtuple('Evenement', text_obj['fields'])

##Creation de la DataFrame de la premiere url
data = pd.DataFrame([k for k in text_obj["values"]])
frame = [data]

##On itere sur les next url
nexturl = ''
while text_obj.get('next'):
    nexturl = text_obj['next']
    r = requests.get(nexturl)
    text_obj = r.json()
    df2 = pd.DataFrame([k for k in text_obj["values"]]);
    frame.append(df2)

data = pd.concat(frame) # nb = 5048 elements

#data.index = data['id']
#data = data.rename(columns={'id': 'idGrandLyon'})

def changeIfNull(row) :
    if row['type_detail']== '':
        row['type_detail'] = row['type']
    return row['type_detail']

data['type_detail'] = data.apply(changeIfNull, axis=1)


#print(data.info())

#print(data['type_detail'].nunique()) # nb = 659 ou 667 apres correctif des vides par le type
#print(data['type_detail'].unique())
#print(data['type'].unique())
#print(data['codepostal'].unique())

##Recherche d'élément
#print(data[data['nom'].str.contains("Tête d'Or")]['nom'])



## DataFrame to Postegre
from sqlalchemy import create_engine
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
data.to_sql('table_name', engine)