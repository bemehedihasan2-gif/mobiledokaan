# Mobiledokaan

Bangladesh-focused smartphone platform (Next.js + FastAPI + PostgreSQL).

## Quick start

### Frontend
```bash
npm install
cp .env.example .env.local
npm run dev
```

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .\.venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Set DATABASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
alembic upgrade head
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Admin: http://localhost:3000/admin/login

Public site needs no user registration. Wishlist uses localStorage.
