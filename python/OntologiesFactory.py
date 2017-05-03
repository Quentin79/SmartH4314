import requests
import pandas as pd
from pg import DB
from sqlalchemy import create_engine
import json

def requestIBM(noms) :

  data = []
  cmpt = 0
  #print(json.loads(noms))
  for it in noms :
    cmpt = cmpt +1
    if it['index'] <= 4998 :
        continue
    
    #if cmpt % 50 == 0 :
    fic = open("MaSauvegardeFrom4998.txt","w")
    fic.write(str(data))
    fic.close()
    print("SAVE" + str(cmpt))
    
        
    parameters = {
     "version" : "2017-02-27",
     "text": it['nom'],
      "features": {
        "categories": {
          "limit" : 1
        }
      }
    }
    r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze', params=parameters, auth=('098768f6-62f6-45b7-b3cd-04510246e583','tEDBI2O2WIJP'))
    if r.status_code==400 :
        continue
    jsonObject = r.json()
    listCtgr = []

    if jsonObject['categories'] :
      categories = jsonObject['categories'][0]['label']
      listCtgr = categories.split('/')
      listCtgr.pop(0)

    listCtgr.extend(['']*(5-len(listCtgr)))

    param = {
      'idGL': it['index'],
      'label0': listCtgr[0],
      'label1' : listCtgr[1],
      'label2' : listCtgr[2],
      'label3' : listCtgr[3],
      'label4' : listCtgr[4]
    }

    data.append(param)

  return data

def getNoms (db) :
  query = "SELECT index,nom FROM public.\"DataGL4\""
  noms = db.query(query)
  return noms.dictresult()



db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
noms = getNoms(db)
#print noms
data = requestIBM(noms)
print json.dumps(data)
df = pd.DataFrame(data, index=range(4999,4999+len(data) ))


engine = create_engine('postgresql://postgres:admin@172.17.0.4:5432/postgres')
df.to_sql('GLOntology', engine, if_exists = 'append')






