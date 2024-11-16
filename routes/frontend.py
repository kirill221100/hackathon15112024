from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

frontend_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@frontend_router.get('/register')
async def register_user(request: Request):
    return templates.TemplateResponse(
        request=request, name="register.html"
    )

