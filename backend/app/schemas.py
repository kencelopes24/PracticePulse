from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class InstructorCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str

class InstructorUpdate(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    certifications: Optional[str] = None
    specialties: Optional[str] = None
    website: Optional[str] = None
    instagram: Optional[str] = None
    phone: Optional[str] = None
    profile_photo_url: Optional[str] = None

class InstructorResponse(BaseModel):
    id: int
    email: str
    full_name: str
    bio: Optional[str]
    profile_photo_url: Optional[str]
    certifications: Optional[str]
    specialties: Optional[str]
    website: Optional[str]
    instagram: Optional[str]
    average_rating: float
    total_reviews: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class QRCodeCreate(BaseModel):
    class_name: Optional[str] = None

class QRCodeResponse(BaseModel):
    id: int
    code: str
    class_name: Optional[str]
    active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class FeedbackCreate(BaseModel):
    overall_rating: int
    communication_rating: int
    pacing_rating: int
    welcomed_rating: int
    community_rating: int
    knowledge_rating: int
    recommend_rating: int
    favorite_aspect: Optional[str] = None
    suggestions: Optional[str] = None
    experience_level: Optional[str] = None
    neighborhood: Optional[str] = None
    wellness_goal: Optional[str] = None
    is_returning_student: bool = False

class FeedbackResponse(BaseModel):
    id: int
    overall_rating: int
    communication_rating: int
    pacing_rating: int
    welcomed_rating: int
    community_rating: int
    knowledge_rating: int
    recommend_rating: int
    favorite_aspect: Optional[str]
    suggestions: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class AnalyticsSummary(BaseModel):
    average_rating: float
    total_reviews: int
    recommendation_rate: float
    returning_student_percentage: float
    average_communication_rating: float
    average_pacing_rating: float
    average_community_rating: float

class AuthResponse(BaseModel):
    access_token: str
    token_type: str
    user: InstructorResponse
