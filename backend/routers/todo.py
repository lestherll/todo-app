from fastapi import APIRouter
from core.schemas.schema import TodoIn, TodoOut, TodoUpdate
from core.models.database import todo_db
from typing import List
from datetime import datetime


router = APIRouter(
    prefix="/todos", tags=["todos"], responses={404: {"description": "Not found"}}
)


@router.get("/")
async def read_todos() -> List[TodoOut]:
    return todo_db


@router.post("/")
async def create_todos(todo: TodoIn) -> TodoOut:
    new_todo: TodoOut = TodoOut(
        **todo.dict(), author="test_user_1", date_created=datetime.now()
    )
    todo_db.append(new_todo)
    return new_todo
