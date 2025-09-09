from sqlmodel import Session, select
from app.models.blog import Blog


def create_blog(session: Session, title: str, content: str) -> Blog:
    blog = Blog(title=title, content=content)
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


def get_blogs(session: Session):
    return session.exec(select(Blog)).all()

def get_blog(session: Session, id: int):
    return session.get(Blog, id)


def update_blog(session: Session, id: int, title: str, content: str):
    blog = session.get(Blog, id)
    if blog:
        blog.title = title
        blog.content = content
        session.add(blog)
        session.commit()
        session.refresh(blog)
    return blog