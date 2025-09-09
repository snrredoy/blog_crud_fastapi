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

@router.get('/get_blog/{blog_id}', response_model=BlogRead)
def get_blog(blog_id: int, session: Session = Depends(get_session)):
    service = BlogService(session)
    blog = service.get_blog_post(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found.")
    return blog


@router.put('/update_blog/{blog_id}', response_model=BlogRead)
def update_blog(blog_id: int, blog: BlogCreate, session: Session = Depends(get_session)):
    service = BlogService(session)
    update_blog = service.update_blog_post(blog_id, blog)
    if not update_blog:
        raise HTTPException(status_code=404, detail="Blog not found.")
    return update_blog


@router.delete('/delete_blog/{blog_id}')
def delete_blog(blog_id: int, session: Session = Depends(get_session)):
    service = BlogService(session)
    delete_blog = service.delete_blog_post(blog_id)
    if not delete_blog:
        raise HTTPException(status_code=404, detail="Blog not found.")
    return {"details": "Blog deleted successfully."}