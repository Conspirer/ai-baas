from jose import jwt, JWTError
from fastapi import HTTPException, status
from app.core.config import JWT_SECRET_KEY, JWT_ALGORITHM

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )