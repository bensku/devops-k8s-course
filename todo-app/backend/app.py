from pydantic import BaseModel
from fastapi import FastAPI, Request

app = FastAPI()

class Todo(BaseModel):
    text: str

todos: list[Todo] = []

@app.get('/todos')
def get_todos():
    return todos

@app.post('/todos')
def add_todo(todo: Todo):
    todos.append(todo)