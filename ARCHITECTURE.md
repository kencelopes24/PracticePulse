# PracticePulse Architecture

## Overview
PracticePulse is a full-stack web application designed to help independent wellness instructors collect and analyze client feedback.

## Technology Stack

### Backend
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** Firebase Auth
- **API:** RESTful JSON API

### Frontend
- **Framework:** React 18
- **Styling:** Tailwind CSS
- **Charting:** Chart.js, Plotly
- **QR Code:** qrcode.react
- **Routing:** React Router v6
- **Build Tool:** Vite

## Data Model

### Core Entities
1. **Instructor** - Profile, authentication, status tracking
2. **QRCode** - Unique codes per class/session
3. **Feedback** - Anonymous survey responses
4. **Admin** - User management & moderation

## API Endpoints Summary

- `/api/v1/auth` - Registration & login
- `/api/v1/instructors` - Profile management
- `/api/v1/feedback` - Feedback submission & retrieval
- `/api/v1/analytics` - Metrics & trends
- `/api/v1/admin` - Admin operations

## Getting Started

```bash
# Start all services
docker-compose up

# Backend: http://localhost:8000
# Frontend: http://localhost:5173
# Database: localhost:5432
```

## Development Workflow

**Week 1:** Core infrastructure, authentication, instructor registration
**Week 2:** Feedback collection, QR codes, public profiles
**Week 3:** Analytics dashboard, KPIs, trends
**Week 4:** Testing, refinement, deployment

## Key Features
- Secure instructor authentication
- Anonymous feedback collection via QR code
- Interactive analytics dashboards
- Public instructor profiles with testimonials
- Admin moderation portal
- Responsive design with Tailwind CSS

## Security
- Firebase authentication
- Role-based access control
- Anonymous feedback (no PII tracking)
- CORS configuration
- Input validation with Pydantic
- SQL injection prevention via ORM
