from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
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
    # ⚠️ À remplacer par une vraie logique d'authentification
    # Ici on simule que l'utilisateur connecté est "erikayossa"
    username = "erikayossa"

    # 🔍 Requête SQLAlchemy pour récupérer l'utilisateur
    result = await db.execute(
        User.__table__.select().where(User.username == username)
    )
    user = result.fetchone()

    if not user:
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "error": "User not found"
        })

    # 🔁 Convertir en dict pour le template
    user_data = {
        "username": user.username,
        "surname": user.surname,
        "first_name": user.first_name
    }

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": user_data
    })