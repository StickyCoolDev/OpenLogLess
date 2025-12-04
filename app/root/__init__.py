from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.config import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def get_root():
    return templates.TemplateResponse(name="index.html", context={"request": {}})
