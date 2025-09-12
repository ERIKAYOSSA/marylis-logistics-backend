from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.hash import bcrypt
from app.database import SessionLocal
from app.models.user import User

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

# 🔧 Dependency pour obtenir une session DB
async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    # 🔍 Rechercher l'utilisateur dans la base
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()

    # ❌ Si l'utilisateur n'existe pas ou le mot de passe est incorrect
    if not user or not bcrypt.verify(password, user.password_hash):
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Nom d'utilisateur ou mot de passe incorrect"
        })

    # ✅ Connexion réussie → redirection vers le dashboard
    return RedirectResponse(url="/dashboard", status_code=302)