from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class APIKey(Base): #SQLAlchemy model for API keys, maps to "api_keys" table
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)
    key_hash = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
