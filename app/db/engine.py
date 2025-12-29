from sqlalchemy import create_engine
from app.core.config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_size = 5,
    max_overflow = 10,
)
