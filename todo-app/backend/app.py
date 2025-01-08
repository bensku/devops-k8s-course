import os
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException
import psycopg

conninfo = psycopg.conninfo.make_conninfo(dbname='postgres', user='postgres', host='todo-db-svc', password=os.environ['DB_PASSWORD'].replace('\n', ''))
with psycopg.connect(conninfo) as conn:
    with conn.cursor() as cur:
        cur.execute('''CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()

app = FastAPI()

class Todo(BaseModel):
    text: str

todos: list[Todo] = []

@app.get('/todos')
def get_todos():
    with psycopg.connect(conninfo) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT text FROM todos')
            return [Todo(text=row[0]) for row in cur.fetchall()]

@app.post('/todos')
def add_todo(todo: Todo):
    if len(todo.text) > 140:
        print('Todo is too long:', todo.text[:140], '... (truncated)')
        raise HTTPException(status_code=400, detail='Todo is too long')
    with psycopg.connect(conninfo) as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO todos (text) VALUES (%s)', (todo.text,))
            conn.commit()
    print('Todo added:', todo.text)