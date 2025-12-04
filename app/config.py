import os

from pathlib import Path
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from slowapi import Limiter
from slowapi.util import get_remote_address


load_dotenv()

SQLITE_ECHO: bool = os.getenv("SQLITE_ECHO", "false").lower() == "true"
DB_URL: str = os.getenv("DB_URL", "sqlite:///def.db")
BASE_DIR: Path = Path(__file__).resolve().parent


# Initialize templates
templates = Jinja2Templates(
    directory=BASE_DIR / "templates",
)


limiter = Limiter(key_func=get_remote_address)
