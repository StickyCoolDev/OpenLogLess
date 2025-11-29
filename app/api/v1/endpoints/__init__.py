import enum
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.sql.functions import current_timestamp

from app.db.models import Log
from app.db import SessionLocal
from app.schema import LogLevel

router: APIRouter = APIRouter()


class SimpleLog(BaseModel):
    log_message: str
    log_level: LogLevel


@router.post("/logs/")
def create_log(log: SimpleLog):
    db = SessionLocal()
    new_log = Log.Log(
                message=log.log_message,
                created_at=current_timestamp(),
                log_level=log.log_level,
                )
    db.add(new_log)
    db.commit()


    return {"ok": True, "message": "log created successfully", "code": "log/created", }
