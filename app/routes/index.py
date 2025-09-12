from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/index")
async def show_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})