from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from uuid import UUID
from . import validate_api_token


router = APIRouter(prefix="/", tags=["Panel"])
templates = Jinja2Template(directory="templates")


@router.get("", response_class=HTMLResponse)
async def get_index_page(
        request: Request
):
    return templates.TemplateResponse("index.html")

