from flask import Flask
from FacebookAPI import FacebookAPI
from pg import DB

app = Flask(__name__)

@app.route('/engine/<token>', methods=['GET', 'POST'])
def main(token):
	
	db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
	myFacebook = FacebookAPI(access_token = token)
	likes = myFacebook.getNamesFromFacebookLikes()

	json_response=fetchData(db,likes)
	#print (json_response)
	return json_response


@app.route('/test', methods=['GET', 'POST'])
def main():
	return "hello world"
