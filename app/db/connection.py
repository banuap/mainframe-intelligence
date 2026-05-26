"""Database connection utilities."""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.config import settings


def get_engine() -> Engine:
    """Create a SQLAlchemy engine using the configured DATABASE_URL."""
    return create_engine(settings.database_url, pool_pre_ping=True)
