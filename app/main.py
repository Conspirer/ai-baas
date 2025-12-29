from fastapi import FastAPI
from app.db.connection import get_connection
from sqlalchemy import text
from app.db.engine import engine
from app.db.session import SessionLocal
from app.models.user import User

app = FastAPI() #Server created


@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/hello")
def hello_message():
    return {"message": "hello"}

@app.get("/status")
def status_message():
    return {"check": "okay"}

@app.get("/square/{number}")
def square(number : int):
    return {"number": number, "square": number*number}

@app.get("/greet")
def greet(name: str = "guest"):
    return {"greeting": f"Hello, {name}"}

@app.get("/users")
def list_users():
    db = SessionLocal() #Creates new session, borrows connection from the pool
    try:
        users = db.query(User).all() #SQLAlchemy used instead of direct SQL commands
        return {"users": [
            {"id": u.id, "email":u.email, "created_at": u.created_at}
            for u in users
        ]}
    finally:
        db.close() #Session ended, connection returned to pool
