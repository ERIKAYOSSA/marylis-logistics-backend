from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/logout")
async def logout_user():
    # 🔐 Si tu utilises un système de session ou JWT plus tard,
    # c'est ici que tu effaceras le cookie ou le token.
    # Exemple (avec cookies) :
    # response = RedirectResponse(url="/index", status_code=302)
    # response.delete_cookie("access_token")
    # return response

    # Pour l'instant, simple redirection vers la page d'accueil
    return RedirectResponse(url="/index", status_code=302)