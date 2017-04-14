from flask import Flask
from facebookAPI import getNamesFromFacebookLikes
from pg import DB

app = Flask(__name__)

@app.route('/engine/<token>', methods=['GET', 'POST'])
def main(token):
	
	db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
	
	likes=getNamesFromFacebookLikes(token)
	json_response=fetchData(db,likes)
	return json_response
