from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Instructor
from app.schemas import InstructorCreate, InstructorResponse, AuthResponse

router = APIRouter()

@router.post("/register", response_model=dict)
async def register(instructor: InstructorCreate, db: Session = Depends(get_db)):
    existing = db.query(Instructor).filter(Instructor.email == instructor.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    return {
        "message": "Registration successful. Pending admin approval.",
        "email": instructor.email
    }

@router.post("/login", response_model=dict)
async def login(email: str, password: str, db: Session = Depends(get_db)):
    return {
        "message": "Login successful",
        "access_token": "placeholder-token",
        "token_type": "bearer"
    }

@router.post("/logout")
async def logout():
    return {"message": "Logged out successfully"}
