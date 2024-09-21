from fastapi import FastAPI

app = FastAPI()

counter = 0

@app.get("/pingpong")
def read_root():
    global counter
    counter += 1
    # with open('/var/ping-count/count', 'w') as f:
    #     f.write(str(counter))
    return f'pong {counter - 1}'

@app.get('/count')
def get_count():
    return str(counter)