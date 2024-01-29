
"""
Module to implement the user model
"""
import enum
from pydantic import BaseModel, field_validator
from typing import Optional
from busapp.apputils.app_logger import applog

# ------------------------------------------------------

class Roles(enum.Enum):
    SELLER = "seller"
    BUYER = "buyer"


class UserWoId(BaseModel):
    name: str
    role: Roles

class User(UserWoId):
    id: int
