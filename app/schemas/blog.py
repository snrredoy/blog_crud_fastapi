from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None