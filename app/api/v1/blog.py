from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.blog import BlogCreate, BlogRead
from app.services.blog_service import BlogService
from app.db.session import get_session

router = APIRouter(prefix="/api/v1", tags=['Blogs'])

@router.post('/blog_create', response_model=BlogRead)
def create_blog(blog: BlogCreate, session: Session = Depends(get_session)):
    service = BlogService(session)
    return service.create_blog_post(blog)

@router.get('/all_blogs', response_model=list[BlogRead])
def get_blogs(session: Session = Depends(get_session)):
    service = BlogService(session)
    return service.get_blogs_post()