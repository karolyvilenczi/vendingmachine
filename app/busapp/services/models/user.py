
"""
Module to implement the user model
"""
from pydantic import BaseModel, field_validator
from busapp.apputils.app_logger import applog

# ------------------------------------------------------

class User(BaseModel):    
    name: str
    role: str
    id:int

class UserResponse(BaseModel):    
    name: str
    role: str
    