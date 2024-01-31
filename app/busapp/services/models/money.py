
"""
Module to implement the user model
"""
from pydantic import BaseModel#, field_validator
from busapp.apputils.app_logger import applog

# ------------------------------------------------------
class Coin(BaseModel): 
    face_value: int
  

    # @field_validator('face_value')
    # @classmethod
    # def face_value_must_be_from_a_range_of_allowed_values(cls, fvalue:int) -> int:
    #     allowed_cent_face_values = [5, 10, 20, 50, 100]
        
    #     if fvalue not in allowed_cent_face_values:
    #         raise ValueError("Coin face value can be 5, 10, 20, 50 and 100 cent")

    #     return fvalue