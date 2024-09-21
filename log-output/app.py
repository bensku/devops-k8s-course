import datetime
import threading
import time
import uuid
from fastapi import FastAPI

app = FastAPI()

random_str = str(uuid.uuid4())
last_time = datetime.datetime.now()

def read_time():
    with open('/var/shared/time', 'r') as f:
        return f.read()

def read_ping_count():
    try:
        with open('/var/ping-count/count', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return '0'

def update_status():
    while True:
        print(read_time(), random_str, flush=True)
        print('Pings / pongs:', read_ping_count(), flush=True)
        time.sleep(5)

threading.Thread(target=update_status).start()

@app.get("/status")
def read_root():
    return {'time': read_time(), 'status': random_str, 'pingcount': int(read_ping_count())}