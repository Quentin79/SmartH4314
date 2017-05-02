import requests
import pandas
from pg import DB
from sqlalchemy import create_engine


def requestIBM(noms) :

  data = []

  for nom in noms :
    parameters = {
     "version" : "2017-02-27",
     "text": nom,
      "features": {
        "categories": {
          "limit" : 1
        }
      }
    }

    r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze', params=parameters, auth=('dc479c4a-de18-4be3-9095-8bb3fc537b58','DuxBm28zBvaB'))

    categories = r.json()['categories'][0]['label']

    listCtgr = categories.split('/')
    listCtgr.pop(0)

    listCtgr.extend(['']*(5-len(listCtgr)))

    param = {
      'nom': nom,
      'label0': listCtgr[0],
      'label1' : listCtgr[1],
      'label2' : listCtgr[2],
      'label3' : listCtgr[3],
      'label4' : listCtgr[4]
    }

    data.append(param)

  return data

def getNoms (db) :
  query = "SELECT nom FROM public.\"DataGL4\" "
  noms = db.query(query)
  return noms.getresult()



db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
noms = getNoms(db)

data = requestIBM(noms)
df = pd.DataFrame(data)


engine = create_engine('postgresql://postgres:admin@172.17.0.4:5432/postgres')
df.to_sql('GLOntology', engine)






