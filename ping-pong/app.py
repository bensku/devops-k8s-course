import os
from fastapi import FastAPI
import psycopg

app = FastAPI()

counter = 0

conninfo = psycopg.conninfo.make_conninfo(dbname='postgres', user='postgres', host='pingpong-db-svc', password=os.environ['DB_PASSWORD'].replace('\n', ''))

# Create database if it doesn't exist
# (in real world, this would use a proper migration tool)
with psycopg.connect(conninfo) as conn:
    with conn.cursor() as cur:
        cur.execute('''CREATE TABLE IF NOT EXISTS pingpong (
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()

@app.get("/pingpong")
def read_root():
    with psycopg.connect(conninfo) as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO pingpong (timestamp) VALUES (NULL)')
            conn.commit()
        with conn.cursor() as cur:
            cur.execute('SELECT COUNT(*) FROM pingpong')
            return f'pong {cur.fetchone()[0] - 1}'

@app.get('/count')
def get_count():
    with psycopg.connect(conninfo) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT COUNT(*) FROM pingpong')
            return str(cur.fetchone()[0])