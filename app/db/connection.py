import psycopg2
from app.core.config import(
    DB_NAME, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
)

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )