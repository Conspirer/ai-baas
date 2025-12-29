from sqlalchemy.orm import sessionmaker
from app.db.engine import engine

SessionLocal = sessionmaker (
    bind = engine, #Ask the engine for a DB connection
    autoflush = False, #No auto-sync changes
    autocommit = False, #Saved only when committed, not automatically
)