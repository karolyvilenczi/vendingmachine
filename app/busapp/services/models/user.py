
"""
Module to implement the user model
"""
from pydantic import BaseModel#, field_validator
from typing import Optional
from busapp.apputils.app_logger import applog

# ------------------------------------------------------
class User(BaseModel):
    id:Optional[int] = 0
    name:str
    role:str
    deposit:Optional[int] = 0
