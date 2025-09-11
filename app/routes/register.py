from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    create_username: str = Form(...),
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
    terms: bool = Form(...),
    marketing: bool = Form(False)
):
    if new_password != confirm_password:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Passwords do not match"
        })

    # 🔐 Ici tu peux ajouter la logique d'enregistrement en base de données

    return RedirectResponse(url="/login", status_code=302)