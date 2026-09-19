# Mobiledokaan

Bangladesh smartphone information platform (Next.js + FastAPI + PostgreSQL).

**GitHub:** https://github.com/bemehedihasan2-gif/mobiledokaan

## Full source upload from PC

This repo has scaffolding. Upload the complete project from your extracted ZIP:

```bash
cd mobiledokaan
git init
git remote add origin https://github.com/bemehedihasan2-gif/mobiledokaan.git
git branch -M main
git add .
git commit -m "Complete Mobiledokaan source"
git push -u origin main --force
```

## Local setup

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
# Windows: .\\.venv\\Scripts\\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Admin: http://localhost:3000/admin/login
