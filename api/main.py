from flask import Flask
from sqlalchemy import create_engine
import pandas as pd
import time
time.sleep(10)

app = Flask(__name__)


#change for your POSTGRES credentials
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
POSTGRES_ADDRES = ''
POSTGRES_DATABASE = ''

engine = create_engine(
    f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_ADDRES}/{POSTGRES_DATABASE}'
)

connection = engine.connect()

@app.route('/all_articles')
def all_articles():
    data = pd.read_sql('select * from articles',connection)
    return data.to_json(orient="records")

@app.route('/last_article')
def last_articles():
    data = pd.read_sql('select * from articles order by "date" desc limit 1',connection)
    return data.to_json(orient="records")