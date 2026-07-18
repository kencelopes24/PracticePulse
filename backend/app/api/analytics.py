from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models import Feedback, Instructor
from app.schemas import AnalyticsSummary

router = APIRouter()

@router.get("/me", response_model=AnalyticsSummary)
async def get_my_analytics(db: Session = Depends(get_db)):
    return {"message": "Implement with auth"}

@router.get("/instructor/{instructor_id}", response_model=AnalyticsSummary)
async def get_instructor_analytics(
    instructor_id: int,
    db: Session = Depends(get_db)
):
    feedbacks = db.query(Feedback).filter(
        Feedback.instructor_id == instructor_id,
        Feedback.is_approved == True
    ).all()
    
    if not feedbacks:
        return {
            "average_rating": 0.0,
            "total_reviews": 0,
            "recommendation_rate": 0.0,
            "returning_student_percentage": 0.0,
            "average_communication_rating": 0.0,
            "average_pacing_rating": 0.0,
            "average_community_rating": 0.0
        }
    
    total = len(feedbacks)
    returning = sum(1 for f in feedbacks if f.is_returning_student)
    
    analytics = {
        "average_rating": sum(f.overall_rating for f in feedbacks) / total,
        "total_reviews": total,
        "recommendation_rate": sum(f.recommend_rating for f in feedbacks) / total / 5 * 100,
        "returning_student_percentage": (returning / total * 100) if total > 0 else 0,
        "average_communication_rating": sum(f.communication_rating for f in feedbacks) / total,
        "average_pacing_rating": sum(f.pacing_rating for f in feedbacks) / total,
        "average_community_rating": sum(f.community_rating for f in feedbacks) / total
    }
    
    return analytics

@router.get("/instructor/{instructor_id}/trends")
async def get_instructor_trends(
    instructor_id: int,
    months: int = 12,
    db: Session = Depends(get_db)
):
    return {"message": "Implement trends"}

@router.get("/instructor/{instructor_id}/themes")
async def get_common_themes(instructor_id: int, db: Session = Depends(get_db)):
    return {"positive_themes": [], "improvements": []}
