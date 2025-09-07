from pydantic import BaseModel
from datetime import datetime

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime