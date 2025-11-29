from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from typing import Iterator

from app import config


engine = create_engine(config.DB_URL, echo=config.SQLITE_ECHO)

Base = declarative_base()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Iterator[Session]:
    """
    Creates a new database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
