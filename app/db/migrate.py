from app.db import Base, engine
from app.db.models import Log


def create_tables():
    """
    Creates all tables defined in the Base.metadata object
    in the database connected to the engine.
    """
    print("Attempting to create all database tables...")
    
    # This is the single, powerful command that creates the tables
    # if they do not already exist in the database.
    Base.metadata.create_all(bind=engine)
    
    print("Database tables created successfully (or already existed).")

if __name__ == "__main__":
    create_tables()
