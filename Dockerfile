FROM python:2
RUN pip install Flask
RUN pip install pandas
RUN pip install requests
RUN pip install sqlalchemy
RUN pip install psycopg2
RUN pip install PyGreSQL
RUN pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk
ENV FLASK_APP /usr/src/myapp/server.py
ENV FLASK_DEBUG 1
