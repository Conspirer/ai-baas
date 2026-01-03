from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel): #Pydantic model for user creation and validation
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)