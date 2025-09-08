from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API Marylis Logistics 🚚"}