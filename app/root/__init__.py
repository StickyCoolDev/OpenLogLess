from os import stat
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.config import templates

router = APIRouter()


def static_template(filename: str):
    return templates.TemplateResponse(name=filename, context={"request": {}})


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def get_root():
    return static_template("index.html")


@router.get("/signup", response_class=HTMLResponse, include_in_schema=False)
def get_signup():
    return static_template("signup_page.html")
