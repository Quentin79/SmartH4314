#! /bin/bash

pip install Flask
pip install pandas
pip install requests
pip install sqlalchemy
pip install psycopg2
pip install PyGreSQL
export FLASK_APP=server.py
flask run --host=0.0.0.0
