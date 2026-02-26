"""
Database URL
------------

Build database connection URL from environment variables.
"""

from os import getenv
from urllib.parse import quote


def build_db_url() -> str:
    """Build database URL from environment variables or DATABASE_URL.

    Uses the psycopg3 driver so SQLAlchemy does not require psycopg2.
    """
    # Prefer a full DATABASE_URL if provided (e.g. from .env or deployment env)
    database_url = getenv("DATABASE_URL")
    if database_url:
        # Normalize scheme for SQLAlchemy + psycopg3
        # if database_url.startswith("postgres://"):
        #     database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)
        # elif database_url.startswith("postgresql://") and "+psycopg" not in database_url:
        #     database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)
        return database_url

    # Fallback to individual DB_* env vars
    driver = getenv("DB_DRIVER", "postgresql+psycopg")
    user = getenv("DB_USER", "ai")
    password = quote(getenv("DB_PASS", "ai"), safe="")
    host = getenv("DB_HOST", "localhost")
    port = getenv("DB_PORT", "5432")
    database = getenv("DB_DATABASE", "ai")
    return f"{driver}://{user}:{password}@{host}:{port}/{database}"


db_url = build_db_url()
