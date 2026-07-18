from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Instructor, QRCode
from app.schemas import InstructorResponse, InstructorUpdate, QRCodeResponse, QRCodeCreate
import uuid

router = APIRouter()

@router.get("/me", response_model=InstructorResponse)
async def get_current_instructor(db: Session = Depends(get_db)):
    return {"message": "Implement with auth"}

@router.get("/{instructor_id}", response_model=InstructorResponse)
async def get_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor

@router.put("/me", response_model=InstructorResponse)
async def update_instructor(
    update_data: InstructorUpdate,
    db: Session = Depends(get_db)
):
    return {"message": "Implement with auth"}

@router.post("/me/qr-codes", response_model=QRCodeResponse)
async def create_qr_code(
    qr_data: QRCodeCreate,
    db: Session = Depends(get_db)
):
    return {"message": "Implement with auth"}

@router.get("/me/qr-codes", response_model=list)
async def get_qr_codes(db: Session = Depends(get_db)):
    return []

@router.get("/search", response_model=list)
async def search_instructors(
    name: str = None,
    specialty: str = None,
    neighborhood: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Instructor).filter(Instructor.status == "approved")
    
    if name:
        query = query.filter(Instructor.full_name.ilike(f"%{name}%"))
    if specialty:
        query = query.filter(Instructor.specialties.ilike(f"%{specialty}%"))
    
    return query.all()
