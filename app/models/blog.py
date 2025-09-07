from sqlmodel import SQLModel, Field
from datetime import datetime

class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
