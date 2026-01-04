from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models.api_usage import APIUsage
from app.models.api_key import APIKey

def get_user_usage(db: Session, user_id: int): #db: Session does not open a connection, it just demands one as the function is called.

    last_24h = datetime.now(timezone.utc) - timedelta(hours=24)

    total_requests = (
        db.query(APIUsage)
        .join(APIKey)
        .filter(APIKey.user_id == user_id)  # Join to filter by user_id
        .count()
    )

    requests_last_24h = (
        db.query(APIUsage)
        .join(APIKey)
        .filter(
            APIKey.user_id == user_id,
            APIUsage.timestamp >= last_24h
        )
        .count()
    )

    per_key_usage = (
        db.query(APIKey.id, func.count(APIUsage.id))
        .join(APIUsage)
        .filter(APIKey.user_id == user_id)
        .group_by(APIKey.id)
        .all()
    )

    return {
        "total_requests": total_requests,
        "requests_last_24h": requests_last_24h,
        "per_api_key": {
            str(key_id): count for key_id, count in per_key_usage
            }
    }