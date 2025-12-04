import hashlib
import secrets

from fastapi import APIRouter, Request
from pydantic import BaseModel
from sqlalchemy.sql.functions import current_timestamp

from app.db.models import Log
from app.db import SessionLocal
from app.db.models.User import User
from app.schema import LogLevel
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



@router.get("signup")
@limiter.limit("20/minute")
def signup(request : Request, response: Response):
    user_name = request.query_params.get("user_name")
    password = request.query_params.get("password")
    if not password:
        return {
            "ok"      : False,
            "message" : "missing passsword"
        }
    salt = secrets.token_bytes(16)
    
    iterations = 390000 

    hashed_password = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        iterations
    )

    
