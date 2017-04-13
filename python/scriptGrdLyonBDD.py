from collections import namedtuple
import pandas as pd
import requests

from modifString import modifierString


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

data = pd.concat(frame, ignore_index= True) # nb = 5048 elements

#data.index = data['id']
#data = data.rename(columns={'id': 'idGrandLyon'})

def changeIfNull(row) :
    if row['type_detail']== '':
        row['type_detail'] = row['type']
    return row['type_detail']

data['type_detail'] = data.apply(changeIfNull, axis=1)
data['type_detail_normalize'] = data['type_detail'].apply(modifierString)
data['nom_normalize'] = data['nom'].apply(modifierString)
data['type_normalize'] = data['type'].apply(modifierString)


#print(data['type_detail'].nunique()) # nb = 659 ou 667 apres correctif des vides par le type
#print(data['type_detail'].unique())
#print(data['type'].unique())
#print(data['codepostal'].unique())

#print(data[data.duplicated()])
##Recherche d'element
#print(data[data['nom'].str.contains("Tete d'Or")]['nom'])


## DataFrame to Postegre
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:admin@172.17.0.4:5432/postgres')
data.to_sql('DataGL4', engine)

#dfDoublon = pd.concat(g for _, g in data.groupby("nom") if len(g) > 1)

