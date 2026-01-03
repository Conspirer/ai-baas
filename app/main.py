from fastapi import FastAPI
from app.db.connection import get_connection
from sqlalchemy import text
from app.db.engine import engine
from app.db.session import SessionLocal
from app.models.user import User
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.db.session import SessionLocal
from app.models.user import User

from app.schemas.auth import LoginRequest
from app.core.security import verify_password
from app.core.jwt import create_access_token



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

@app.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate):
    db = SessionLocal()
    try:
        new_user = User(
            email=user.email,
            password_hash = hash_password(user.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "id": new_user.id,
            "email": new_user.email,
            "created_at": new_user.created_at
        }
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    finally:
        db.close()

@app.post("/login")
def login(credentials: LoginRequest):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == credentials.email).first()

        if not user or not verify_password(credentials.password, user.password_hash):
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )
        
        token = create_access_token({"sub": str(user.id)})

        return {"access_token": token, "token_type": "bearer"}
    
    finally:
        db.close()