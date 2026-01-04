from fastapi import Header, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.api_key import APIKey
from app.core.api_keys import hash_api_key

def get_api_key(x_api_key: str = Header(...)): #The ... after Header makes it mandatory to contain the string
    db: Session = SessionLocal()
    try:
        key_hash = hash_api_key(x_api_key)
        key = db.query(APIKey).filter(APIKey.key_hash == key_hash).first()

        if not key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid API Key"
            )
        
        return {
            "user_id": key.user_id,
            "api_key_id": key.id
        }
    finally:
        db.close()

