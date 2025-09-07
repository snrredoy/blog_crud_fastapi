from app.repositories.blog import create_blog
from sqlmodel import Session
from app.schemas.blog import BlogCreate


class BlogService:
    def __init__(self, session: Session):
        self.session = session

    def create_blog_post(self, blog_in: BlogCreate):
        return create_blog(self.session, blog_in.title, blog_in.content)