from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import ContactMessage
from database import SessionLocal

router = APIRouter(prefix="/contact", tags=["contact"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/send")
def send_message(name: str, email: str, message: str, db: Session = Depends(get_db)):
    msg = ContactMessage(name=name, email=email, message=message)
    db.add(msg)
    db.commit()
    return {"msg": "Message sent"}