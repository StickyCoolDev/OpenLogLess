import hashlib
import secrets

from fastapi import APIRouter, Request, Response
from pydantic import BaseModel
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import or_
from app.db.models import Log
from app.db import SessionLocal
from app.db.models.User import User
from app.schema import LogLevel, UserTier
from app.config import limiter


router: APIRouter = APIRouter()


class CreateLog(BaseModel):
    log_message: str
    log_level: LogLevel


@router.post("/logs/", tags=["logs"])
@limiter.limit("2/second")
def create_log(request: Request, log: CreateLog):
    """
    Create a new log. with the following **paramaters**:
    ```schema
        1. log_message : String
        2. log_level : ENUM{
            "DEBUG"
            "INFO"
            "WARN"
            "ERROR"
            "FATAl"
        }
    ```
    """
    db = SessionLocal()
    new_log = Log(
        message=log.log_message,
        created_at=current_timestamp(),
        log_level=log.log_level,
    )
    db.add(new_log)
    db.commit()

    return {
        "ok": True,
        "message": "log created successfully",
        "code": "log/created",
    }


class GetLog(BaseModel):
    log_filter: LogLevel = LogLevel.INFO
    get_id: bool = False


@router.get(
    "/log/",
    tags=["logs"],
)
@limiter.limit("1/second")
def get_log(request: Request):
    session = SessionLocal()
    logs = session.query(Log).where(Log.log_level != "DEBUG").all()

    return logs


from fastapi import Form


@router.post("/signup", tags=["auth"])
@limiter.limit("20/minute")
def signup(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
):
    db = SessionLocal()

        # Check if email OR username already exists
    existing = db.query(User).filter(
        or_(
            User.email == email,
            User.user_name == email
        )
    ).first()
    
    if existing:
        return {
            "ok": False,
            "message": "User already registered",
            "code": "signup/exists",
        }

    salt = secrets.token_bytes(16)
    iterations = 390000

    hashed_password = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations,
    )

    user = User(
        email=email,
        user_name=email,
        salt=salt.hex(),
        hashed_password=hashed_password.hex(),
        is_active=True,
        created_at=current_timestamp(),
        user_tier=UserTier.FREE_PLAN,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "ok": True,
        "message": "user created",
        "code": "signup/success",
        "user_id": user.id,
    }
