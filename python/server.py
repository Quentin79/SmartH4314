from flask import Flask

from pg import DB

app = Flask(__name__)

@app.route('/engine', methods=['GET', 'POST'])
def main():
	
	db = DB(dbname='postgres', host='172.17.0.4', port=5432, user='postgres', passwd='admin')
	token =""
	
	likes=getLikesByLucaMyBitch(token)
	json_response=fetchData(db,likes)
	return json_response
