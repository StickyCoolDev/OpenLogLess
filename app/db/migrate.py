from app.db import Base, engine
from app.db.models import Log, User, Token


def create_tables():
    """
    Creates all tables defined in the Base.metadata object
    in the database connected to the engine.
    """
    print("Attempting to create all database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully (or already existed).")


if __name__ == "__main__":
    create_tables()
