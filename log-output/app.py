import datetime
import threading
import time
import uuid
from fastapi import FastAPI

app = FastAPI()

random_str = str(uuid.uuid4())
last_time = datetime.datetime.now()

def update_status():
    while True:
        last_time = datetime.datetime.now()
        print(last_time, random_str, flush=True)
        time.sleep(5)

threading.Thread(target=update_status).start()

@app.get("/status")
def read_root():
    return {'time': last_time, 'status': random_str}