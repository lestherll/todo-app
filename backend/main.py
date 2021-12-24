from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import todo


app = FastAPI()

app.include_router(todo.router)

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
