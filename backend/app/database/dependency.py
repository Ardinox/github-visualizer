from collections.abc import Generator
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

def get_db() -> Generator[Session, None, None]:
    # Create a database session for the current request
    db = SessionLocal()

    try:
        # Provide the session to the FastAPI endpoint
        yield db
    finally:
        # Always close the session after the request finishes
        db.close()