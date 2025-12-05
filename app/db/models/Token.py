from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    String,
    Integer,
)
import secrets

from app.db import Base
from app.schema import TokenPermison


def create_token() -> str:
    return secrets.token_hex(16)


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, index=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)

    token = Column(
        String(32),
        CheckConstraint("LENGTH(token) <= 32", name="token_max_length"),
        nullable=False,
        unique=True,
    )

    is_active = Column(Boolean, nullable=False, default=True)
    token_permision = Column(Enum(TokenPermison), nullable=False)
