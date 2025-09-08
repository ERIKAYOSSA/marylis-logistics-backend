from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Marylis Logistics</title>
        <style>
            body {
                background-color: #f0f8ff;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding: 50px;
                color: #003366;
            }
            h1 {
                font-size: 3em;
                color: #006400;
            }
            p {
                font-size: 1.2em;
                margin-top: 20px;
            }
            .logo {
                width: 120px;
                margin-bottom: 20px;
            }
            .btn {
                margin-top: 30px;
                padding: 12px 24px;
                background-color: #006400;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 1em;
                cursor: pointer;
                text-decoration: none;
            }
            .btn:hover {
                background-color: #004d00;
            }
        </style>
    </head>
    <body>
        <img src="https://via.placeholder.com/120x120.png?text=Logo" alt="Marylis Logo" class="logo">
        <h1>Bienvenue chez Marylis Logistics 🚚</h1>
        <p>Suivi de colis, transport international, et service client de qualité.</p>
        <a href="/track/123456" class="btn">Suivre un colis</a>
    </body>
    </html>
    """