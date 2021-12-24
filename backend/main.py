from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List

from schemas import TodoIn, TodoOut

app = FastAPI()

origins = [
    "http://localhost:5000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


todo_db: List[TodoOut] = [
    TodoOut(
        title="First Todo",
        content="A todo list content test",
        author="test_user_1",
        date_created=datetime.now()
        ),
    TodoOut(
        title="Second Todo",
        content="Test content 2",
        author="test_user_1",
        date_created=datetime.now()
        )
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/todos")
async def read_todos() -> List[TodoOut]:
    return todo_db


@app.post("/todos")
async def create_todos(todo: TodoIn) -> TodoOut:
    new_todo: TodoOut = TodoOut(**todo.dict(), author="test_user_1", date_created=datetime.now())
    todo_db.append(new_todo)
    return new_todo
