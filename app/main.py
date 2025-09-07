from fastapi import FastAPI
from app.api.v1 import blog
from app.db.session import engine
from sqlmodel import SQLModel

app = FastAPI(title="Blog App")

app.include_router(blog.router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)