import email
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date, datetime
from uuid import uuid4 as uuid

class User(BaseModel):
    id : Optional[int]
    name : str = Field (...,
                        min_length=50,
                        max_length=255)
    email: EmailStr = Field(
                        default="example@example.com")
    password: str = Field(...,
                          min_length=8,
                          max_length=255)
    