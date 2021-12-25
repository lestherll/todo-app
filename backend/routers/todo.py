from fastapi import APIRouter
from core.models.model import Todo, TodoIn, TodoOut, TodoUpdate
from typing import List
from datetime import datetime


router = APIRouter(
    prefix="/todos", tags=["todos"], responses={404: {"description": "Not found"}}
)


@router.get("/")
async def read_todos() -> List[TodoOut]:
    return await TodoOut.from_queryset(Todo.all())


@router.post("/")
async def create_todos(todo: TodoIn) -> TodoOut:

    todo_obj = await Todo.create(
        **todo.dict(exclude_unset=True), author="test_user1", created_at=datetime.now()
    )
    return await TodoOut.from_tortoise_orm(todo_obj)


@router.put("/")
async def update_todo(todo: TodoUpdate) -> TodoOut:
    await Todo.filter(id=todo.id).update(
        **todo.dict(exclude_unset=True, exclude={"id"})
    )
    return await TodoOut.from_queryset_single(Todo.get(id=todo.id))
