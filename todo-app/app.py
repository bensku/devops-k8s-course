import os
import threading
import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

def update_status():
    path = '/var/cache/random.jpg'
    while True:
        if not os.path.isfile(path) or time.time() - os.path.getmtime(path) > 3600:
            img = requests.get('https://picsum.photos/1200')
            with open(path, 'wb') as f:
                f.write(img.content)
            print('Updated', path, flush=True)
        time.sleep(5) # Due to potential container reboots, we can't just wait for an hour

threading.Thread(target=update_status).start()

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/cache', StaticFiles(directory='/var/cache'), name='cache')

@app.get('/health')
def health():
    return {'status': 'green'}

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(request=request, name='index.html', context={})
