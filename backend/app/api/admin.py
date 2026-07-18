from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Instructor, Feedback, InstructorStatus

router = APIRouter()

@router.get("/instructors")
async def get_pending_instructors(db: Session = Depends(get_db)):
    instructors = db.query(Instructor).filter(
        Instructor.status == InstructorStatus.PENDING
    ).all()
    return instructors

@router.post("/instructors/{instructor_id}/approve")
async def approve_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    
    instructor.status = InstructorStatus.APPROVED
    db.commit()
    return {"message": "Instructor approved"}

@router.post("/instructors/{instructor_id}/reject")
async def reject_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    
    instructor.status = InstructorStatus.REJECTED
    db.commit()
    return {"message": "Instructor rejected"}

@router.get("/feedback/pending")
async def get_pending_feedback(db: Session = Depends(get_db)):
    return []

@router.post("/feedback/{feedback_id}/approve")
async def approve_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    feedback.is_approved = True
    db.commit()
    return {"message": "Feedback approved"}

@router.delete("/feedback/{feedback_id}")
async def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    db.delete(feedback)
    db.commit()
    return {"message": "Feedback deleted"}

@router.get("/metrics")
async def get_platform_metrics(db: Session = Depends(get_db)):
    total_instructors = db.query(Instructor).count()
    approved_instructors = db.query(Instructor).filter(
        Instructor.status == InstructorStatus.APPROVED
    ).count()
    total_feedback = db.query(Feedback).count()
    
    return {
        "total_instructors": total_instructors,
        "approved_instructors": approved_instructors,
        "total_feedback": total_feedback
    }
