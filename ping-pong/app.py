import os
from fastapi import FastAPI, HTTPException
import psycopg

app = FastAPI()

counter = 0

conninfo = psycopg.conninfo.make_conninfo(dbname='postgres', user='postgres', host='pingpong-db-svc', password=os.environ['DB_PASSWORD'].replace('\n', ''))

db_inited = False

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

@app.get('/health')
def health():
    try:
        with psycopg.connect(conninfo) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT 1')
        
        # Initialize database now that we know it's reachable
        if not db_inited:
            with psycopg.connect(conninfo) as conn:
                with conn.cursor() as cur:
                    cur.execute('''CREATE TABLE IF NOT EXISTS pingpong (
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
                    conn.commit()

        return {'status': 'green'}
    except Exception as e:
        print('Health check failed:', e)
        raise HTTPException(status_code=500, detail={'status': 'red'})

@app.get('/')
def root():
    return {}