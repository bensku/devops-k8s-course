import datetime
import os
import threading
import time
import uuid

import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

random_str = str(uuid.uuid4())
last_time = datetime.datetime.now()

with open('/var/config/information.txt', 'r') as f:
    information = f.read()

def read_time():
    with open('/var/shared/time', 'r') as f:
        return f.read()

def read_ping_count():
    res = requests.get('http://ping-pong/count')
    return res.json()

def update_status():
    while True:
        try:
            print('file content:', information)
            print('env variable:', f'MESSAGE={os.environ['MESSAGE']}')
            print(read_time(), random_str, flush=True)
            print('Pings / pongs:', read_ping_count(), flush=True)
        except Exception as e:
            print('Error updating status', e, flush=True)
        time.sleep(5)

threading.Thread(target=update_status).start()

@app.get('/status')
def read_root():
    return {'time': read_time(), 'status': random_str, 'pingcount': int(read_ping_count())}

@app.get('/health')
def health():
    try:
        read_time()
        read_ping_count()
        return {'status': 'green'}
    except Exception as e:
        print('Health check failed:', e)
        raise HTTPException(status_code=500, detail={'status': 'red'})

@app.get('/')
def root():
    return {}