from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app.models.user import User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# 🔧 Dependency pour obtenir une session DB
async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/dashboard")
async def show_dashboard(request: Request, db: AsyncSession = Depends(get_db)):
    # 🔐 Récupère le nom d'utilisateur depuis le cookie
    username = request.cookies.get("username")

    if not username:
        # Si aucun cookie, redirige vers la page de connexion
        return RedirectResponse(url="/login", status_code=302)

    # 🔍 Requête SQLAlchemy pour récupérer l'utilisateur
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()

    if not user:
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "error": "Utilisateur introuvable"
        })

    # 🔁 Données à transmettre au template
    user_data = {
        "username": user.username,
        "surname": user.surname,
        "first_name": user.first_name
    }

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": user_data
    })