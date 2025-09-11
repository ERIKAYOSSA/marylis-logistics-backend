from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.database import SessionLocal
from app.models.user import User
from passlib.hash import bcrypt

router = APIRouter()

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
    code: str = Form(...),
    new_password: str = Form(...),
    confirm_password: str = Form(...),
    marketing: bool = Form(False)
):
    if new_password != confirm_password:
        return HTMLResponse(content="Passwords do not match", status_code=400)

    async with SessionLocal() as session:
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            surname=surname,
            country=country,
            contact_number=contact_number,
            mobile_number=mobile_number,
            code=code,
            password_hash=bcrypt.hash(new_password),
            marketing_opt_in=marketing
        )
        session.add(user)
        await session.commit()

    return RedirectResponse(url="/login", status_code=302)