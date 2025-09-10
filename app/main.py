from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
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

# 📦 Données simulées pour la recherche
sample_data = [
    {
        "title": "Green Logistics",
        "description": "Eco-friendly practices in global supply chains.",
        "link": "#green"
    },
    {
        "title": "Fleet Optimization",
        "description": "Managing inventory at scale with smart routing.",
        "link": "#fleet"
    },
    {
        "title": "Oktoberfest Strategy",
        "description": "Seasonal logistics planning for events.",
        "link": "#oktoberfest"
    },
    {
        "title": "Trend Mapping",
        "description": "Predictive tools for future logistics decisions.",
        "link": "#trend"
    }
]

# 🔍 Route pour la recherche
@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    query = request.query_params.get("q", "").lower()
    results = [item for item in sample_data if query in item["title"].lower() or query in item["description"].lower()]
    return templates.TemplateResponse("search_results.html", {
        "request": request,
        "query": query,
        "results": results
    })

# 🔐 Route GET pour afficher la page de login
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# 🔐 Route POST pour traiter le formulaire de login
@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Exemple simple de vérification (à remplacer par une vraie base de données)
    if username == "admin" and password == "secret":
        response = RedirectResponse(url="/", status_code=302)
        return response
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Nom d'utilisateur ou mot de passe incorrect"
    })