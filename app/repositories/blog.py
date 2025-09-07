from sqlmodel import Session, select
from app.models.blog import Blog


def create_blog(session: Session, title: str, content: str) -> Blog:
    blog = Blog(title=title, content=content)
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog