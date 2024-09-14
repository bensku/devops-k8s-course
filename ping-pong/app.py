from fastapi import FastAPI

app = FastAPI()

counter = 0

@app.get("/pingpong")
def read_root():
    global counter
    counter += 1
    return f'pong {counter - 1}'