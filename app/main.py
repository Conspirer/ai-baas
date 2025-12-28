from fastapi import FastAPI
from app.db.connection import get_connection

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
    conn = get_connection() #Establishes connection
    cur = conn.cursor() #Makes cursor to use for commands using execute

    cur.execute("SELECT id, email, created_at FROM users;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"users": rows}


