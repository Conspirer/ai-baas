from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.api_usage import APIUsage
from app.models.api_key import APIKey

RATE_LIMIT = 100  # Max requests
WINDOW_MINUTES = 60

def rate_limit(api_key_id: int):
    db: Session = SessionLocal()
    try:
        window_start = datetime.now(timezone.utc) - timedelta(minutes=WINDOW_MINUTES)

        usage_count = (
            db.query(APIUsage)
            .filter(
                APIUsage.api_key_id == api_key_id,
                APIUsage.timestamp >= window_start
            )
            .count() #Sliding window rate limiting
        )

        if usage_count >= RATE_LIMIT:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Try again later."
            )
        
        usage = APIUsage(api_key_id=api_key_id)
        db.add(usage)
        db.commit()

    finally:
        db.close()
