from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app.models.user import User
from passlib.hash import bcrypt

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# 🔧 Dependency pour session DB
async def get_db():
    async with SessionLocal() as session:
        yield session

# 🟢 Route GET pour afficher le formulaire
@router.get("/register", response_class=HTMLResponse)
async def show_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# 🟢 Route POST pour traiter l'inscription
@router.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    first_name: str = Form(...),
    surname: str = Form(...),
    country: str = Form(...),
    contact_number: str = Form(...),
    mobile_number: str = Form(""),
    new_password: str = Form(...),
    confirm_password: str = Form(...),
    marketing: bool = Form(False),
    db: AsyncSession = Depends(get_db)
):
    # 🔐 Vérifie si les mots de passe correspondent
    if new_password != confirm_password:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Les mots de passe ne correspondent pas."
        })

    # 🔍 Vérifie si le username existe déjà
    result_user = await db.execute(select(User).where(User.username == username))
    if result_user.scalar_one_or_none():
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Ce nom d'utilisateur est déjà utilisé."
        })

    # 🔍 Vérifie si l'email existe déjà
    result_email = await db.execute(select(User).where(User.email == email))
    if result_email.scalar_one_or_none():
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Cet email est déjà enregistré."
        })

    # ✅ Crée l'utilisateur
    user = User(
        username=username,
        email=email,
        first_name=first_name,
        surname=surname,
        country=country,
        contact_number=contact_number,
        mobile_number=mobile_number,
        password_hash=bcrypt.hash(new_password),
        marketing_opt_in=marketing
    )

    db.add(user)
    await db.commit()

    # 🔁 Redirection vers la page de connexion
    return RedirectResponse(url="/login", status_code=302)