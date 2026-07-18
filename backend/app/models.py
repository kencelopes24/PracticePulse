from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

class UserRole(str, enum.Enum):
    INSTRUCTOR = "instructor"
    ADMIN = "admin"

class InstructorStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class Instructor(Base):
    __tablename__ = "instructors"
    
    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    bio = Column(Text, nullable=True)
    profile_photo_url = Column(String, nullable=True)
    certifications = Column(Text, nullable=True)
    specialties = Column(String, nullable=True)
    website = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    status = Column(Enum(InstructorStatus), default=InstructorStatus.PENDING)
    average_rating = Column(Float, default=0.0)
    total_reviews = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    feedbacks = relationship("Feedback", back_populates="instructor")
    qr_codes = relationship("QRCode", back_populates="instructor")

class QRCode(Base):
    __tablename__ = "qr_codes"
    
    id = Column(Integer, primary_key=True, index=True)
    instructor_id = Column(Integer, ForeignKey("instructors.id"), index=True)
    code = Column(String, unique=True, index=True)
    class_name = Column(String, nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    instructor = relationship("Instructor", back_populates="qr_codes")
    feedbacks = relationship("Feedback", back_populates="qr_code")

class Feedback(Base):
    __tablename__ = "feedbacks"
    
    id = Column(Integer, primary_key=True, index=True)
    instructor_id = Column(Integer, ForeignKey("instructors.id"), index=True)
    qr_code_id = Column(Integer, ForeignKey("qr_codes.id"), nullable=True)
    
    # Survey responses
    overall_rating = Column(Integer)
    communication_rating = Column(Integer)
    pacing_rating = Column(Integer)
    welcomed_rating = Column(Integer)
    community_rating = Column(Integer)
    knowledge_rating = Column(Integer)
    recommend_rating = Column(Integer)
    
    favorite_aspect = Column(Text, nullable=True)
    suggestions = Column(Text, nullable=True)
    
    # Demographics (optional)
    experience_level = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    wellness_goal = Column(String, nullable=True)
    
    is_returning_student = Column(Boolean, default=False)
    is_approved = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    instructor = relationship("Instructor", back_populates="feedbacks")
    qr_code = relationship("QRCode", back_populates="feedbacks")

class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    role = Column(Enum(UserRole), default=UserRole.ADMIN)
    created_at = Column(DateTime, default=datetime.utcnow)
