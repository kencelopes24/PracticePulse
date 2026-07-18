# PracticePulse

A professional feedback and analytics platform for independent wellness instructors (yoga, pilates, meditation, breathwork) to collect anonymous client feedback, monitor trends, and build their professional reputation.

## Project Overview

**Problem:** Independent yoga instructors spend years developing their teaching practice but have limited access to meaningful client feedback beyond occasional conversations or scattered online reviews.

**Solution:** PracticePulse provides a centralized platform where instructors can:
- Collect anonymous client feedback via QR code
- Monitor satisfaction and engagement trends
- Display verified testimonials on a public profile
- Access actionable business intelligence dashboards

## Core Features

### For Instructors
- Secure login and personal dashboard
- Editable professional profile (bio, certifications, specialties, photo gallery)
- QR code generation for feedback collection
- Analytics dashboard with KPIs and trends
- Review management interface

### For Students
- No account required—scan QR code and provide feedback
- Short anonymous survey (satisfaction, pacing, communication, community, etc.)
- Optional demographic information

### For Administrators
- Instructor account approval
- Inappropriate review removal
- Platform activity monitoring
- Metrics export

## Tech Stack

- **Frontend:** React, Tailwind CSS, Plotly/Chart.js
- **Backend:** FastAPI, Python
- **Database:** PostgreSQL
- **Authentication:** Firebase Authentication or Clerk
- **QR Code:** React QR Code
- **Deployment:** Azure App Service, Vercel, or Render

## Project Structure

```
PracticePulse/
├── backend/              # FastAPI server
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models.py      # SQLAlchemy ORM models
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── database.py
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── instructors.py
│   │   │   ├── feedback.py
│   │   │   ├── analytics.py
│   │   │   └── admin.py
│   │   └── services/      # Business logic
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
├── frontend/             # React app
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/     # API client
│   │   ├── styles/
│   │   └── App.jsx
│   ├── package.json
│   └── .env.example
├── docs/                 # Documentation
├── docker-compose.yml    # Local dev environment
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Docker & Docker Compose (optional)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install

# Configure environment
cp .env.example .env
# Edit .env with your API URL

# Start dev server
npm run dev
```

### Using Docker Compose

```bash
docker-compose up -d
```

This starts PostgreSQL, FastAPI backend, and React frontend.

## Development Timeline

- **Week 1:** Core infrastructure, authentication, instructor registration
- **Week 2:** Feedback collection, QR codes, public profiles
- **Week 3:** Analytics dashboard, KPIs, trends
- **Week 4:** Testing, refinement, deployment

## Key Milestones

- [ ] Database schema & auth setup
- [ ] Instructor registration & login
- [ ] Anonymous feedback form & QR code
- [ ] Public instructor profiles
- [ ] Analytics dashboard
- [ ] Admin portal
- [ ] Deployment to production

## Stretch Goals

- Email notifications for new reviews
- PDF performance reports
- Badge system
- Instructor search by neighborhood
- AI-assisted sentiment summaries
- Multi-language support

## Deployment

Ready for deployment to:
- Azure App Service
- Vercel (frontend)
- Render
- Railway

## Contributing

This is a personal project developed during a 4-week fellowship. All code follows standard practices and includes documentation.

## License

MIT
