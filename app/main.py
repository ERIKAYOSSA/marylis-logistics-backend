from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import auth  # 👈 import du module auth
from app.routes import register  # 👈 ajoute register
from app.routes import dashboard
from app.routes import logout
from app.routes import index

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# 🏠 Route pour la page d’accueil
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 🔍 Route de recherche (tu peux aussi la déplacer dans search.py plus tard)
sample_data = [
    {"title": "Green Logistics", "description": "Eco-friendly practices in global supply chains.", "link": "#green"},
    {"title": "Fleet Optimization", "description": "Managing inventory at scale with smart routing.", "link": "#fleet"},
    {"title": "Oktoberfest Strategy", "description": "Seasonal logistics planning for events.", "link": "#oktoberfest"},
    {"title": "Trend Mapping", "description": "Predictive tools for future logistics decisions.", "link": "#trend"}
]

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request): 
    query = request.query_params.get("q", "").lower()
    results = [item for item in sample_data if query in item["title"].lower() or query in item["description"].lower()]
    return templates.TemplateResponse("search_results.html", {
        "request": request,
        "query": query,
        "results": results
    })

# 🔐 Inclusion des routes d'authentification
app.include_router(auth.router)
app.include_router(register.router) 
app.include_router(dashboard.router)
app.include_router(logout.router)
app.include_router(index.router)

