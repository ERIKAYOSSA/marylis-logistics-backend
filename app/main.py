from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 📁 Montre le dossier static (CSS, JS, images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 📁 Dossier des templates HTML
templates = Jinja2Templates(directory="app/templates")

# 🏠 Route pour la page d’accueil
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})