from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import todo, users, auth

from tortoise.contrib.fastapi import register_tortoise
from core.config import settings


app = FastAPI()

app.include_router(todo.router)
app.include_router(users.router)
app.include_router(auth.router)

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


@app.get("/")
async def root():
    return {"message": "This is a todo list"}


register_tortoise(
    app,
    db_url=settings.DB_URI,
    modules={"models": ["core.models.model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
