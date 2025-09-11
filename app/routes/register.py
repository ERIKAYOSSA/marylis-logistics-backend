from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import SessionLocal
from app.models.user import User
from passlib.hash import bcrypt

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

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
    marketing: bool = Form(False)
):
    if new_password != confirm_password:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Passwords do not match"
        })

    async with SessionLocal() as session:
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
        session.add(user)
        await session.commit()

    return RedirectResponse(url="/login", status_code=302)