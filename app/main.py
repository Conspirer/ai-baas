from fastapi import FastAPI
from app.db.connection import get_connection
from sqlalchemy import text
from app.db.engine import engine

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
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, email, created_at FROM users")
        )
        users = result.fetchall()

        return {"users": [dict(row) for row in users]}

