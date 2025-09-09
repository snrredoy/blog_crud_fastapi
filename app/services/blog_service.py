from app.repositories.blog import create_blog, get_blogs, get_blog, update_blog, delete_blog, update_blog_partial
from sqlmodel import Session
from app.schemas.blog import BlogCreate, BlogUpdate


class BlogService:
    def __init__(self, session: Session):
        self.session = session

    def create_blog_post(self, blog_in: BlogCreate):
        return create_blog(self.session, blog_in.title, blog_in.content)
    
    def get_blogs_post(self):
        return get_blogs(self.session)
    
    def get_blog_post(self, blog_id: int):
        return  get_blog(self.session, blog_id)
    
    def update_blog_post(self, id: int, blog_in: BlogCreate):
        return update_blog(self.session, id, blog_in.title, blog_in.content)
    
    def delete_blog_post(self, id: int):
        return delete_blog(self.session, id)
    
    def update_blog_partial_post(self, id: int, blog_update: BlogUpdate):
        return update_blog_partial(self.session, id, blog_update.title, blog_update.content)