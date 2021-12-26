from fastapi import APIRouter
from core.models.model import Todo, TodoIn, TodoOut, TodoUpdate, User
from typing import List
from datetime import datetime


router = APIRouter(
    prefix="/todos", tags=["todos"], responses={404: {"description": "Not found"}}
)


def get_current_user():
    return 1


@router.get("/", response_model=List[TodoOut])
async def read_todos():
    return await TodoOut.from_queryset(Todo.all())


@router.post("/", response_model=TodoOut)
async def create_todo(todo: TodoIn):
    author = await User.get(id=get_current_user())

    todo_obj = await Todo.create(
        **todo.dict(exclude_unset=True), author_id=author, created_at=datetime.now()
    )
    return await TodoOut.from_tortoise_orm(todo_obj)


@router.put("/", response_model=TodoOut)
async def update_todo(todo: TodoUpdate):
    await Todo.filter(id=todo.id).update(
        **todo.dict(exclude_unset=True, exclude=["id"])
    )
    return await TodoOut.from_queryset_single(Todo.get(id=todo.id))


@router.delete("/", response_model=TodoOut)
async def delete_todo(todo_id: int):
    todo_to_delete = await Todo.filter(id=todo_id).get()
    await todo_to_delete.delete()
    return todo_to_delete
