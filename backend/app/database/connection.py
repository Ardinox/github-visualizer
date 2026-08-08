from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# SQLAlchemy engine responsible for managing database connections
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

# Factory for creating database sessions
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)