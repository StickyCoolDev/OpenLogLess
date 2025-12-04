from app.db import Base
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Enum, Integer, String

from app.schema import UserTier


class User(Base):
    """
    SQLalchemy model for user.
    """

    __tablename__ = "users"

    id = Column(Integer, index=True, nullable=False, primary_key=True)
    user_name = Column(
        String(64),
        CheckConstraint("LENGTH(user_name) <= 64", name="user_name_max_length"),
        nullable=False,
        unique=True,
    )
    email = Column(String, nullable=False, unique=True)

    hashed_password = Column(String, nullable=False)
    salt = Column(String, nullable=False)

    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(
        DateTime,
        index=True,
        nullable=False,
    )

    user_tier = Column(Enum(UserTier), nullable=False)

    def __repr__(self) -> str:
        return f"<User user_name={self.user_name}, email={self.email}, tier={self.user_tier}>"
