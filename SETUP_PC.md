# Mobiledokaan — Windows PC Setup

1. Install Node.js 20+, Python 3.11+, PostgreSQL
2. Frontend: npm install && npm run dev
3. Backend: cd backend, create venv, pip install -r requirements.txt, set .env, alembic upgrade head, uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
4. Admin: http://localhost:3000/admin/login
