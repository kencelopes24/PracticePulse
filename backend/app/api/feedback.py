from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Feedback, QRCode, Instructor
from app.schemas import FeedbackCreate, FeedbackResponse
from datetime import datetime

router = APIRouter()

@router.post("/submit/{qr_code}", response_model=dict)
async def submit_feedback(
    qr_code: str,
    feedback_data: FeedbackCreate,
    db: Session = Depends(get_db)
):
    qr = db.query(QRCode).filter(QRCode.code == qr_code).first()
    if not qr or not qr.active:
        raise HTTPException(status_code=404, detail="QR code not found or inactive")
    
    feedback = Feedback(
        instructor_id=qr.instructor_id,
        qr_code_id=qr.id,
        **feedback_data.dict()
    )
    
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    
    instructor = db.query(Instructor).filter(Instructor.id == qr.instructor_id).first()
    if instructor:
        total_feedbacks = db.query(Feedback).filter(Feedback.instructor_id == instructor.id).all()
        if total_feedbacks:
            avg_rating = sum([f.overall_rating for f in total_feedbacks]) / len(total_feedbacks)
            instructor.average_rating = avg_rating
            instructor.total_reviews = len(total_feedbacks)
            db.commit()
    
    return {"message": "Feedback submitted successfully", "feedback_id": feedback.id}

@router.get("/instructor/{instructor_id}", response_model=list)
async def get_instructor_feedback(
    instructor_id: int,
    db: Session = Depends(get_db)
):
    feedbacks = db.query(Feedback).filter(
        Feedback.instructor_id == instructor_id,
        Feedback.is_approved == True
    ).all()
    return feedbacks

@router.get("/me", response_model=list)
async def get_my_feedback(db: Session = Depends(get_db)):
    return []

@router.delete("/{feedback_id}")
async def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    feedback.is_approved = False
    db.commit()
    return {"message": "Feedback removed"}
