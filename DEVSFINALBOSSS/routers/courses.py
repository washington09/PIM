from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Course
from database import SessionLocal

router = APIRouter(prefix="/courses", tags=["courses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add")
def add_course(title: str, description: str, db: Session = Depends(get_db)):
    course = Course(title=title, description=description)
    db.add(course)
    db.commit()
    return {"msg": "Course added"}

@router.get("/list")
def list_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses