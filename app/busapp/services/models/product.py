
"""
Module to implement the product management functions
"""
from pydantic import BaseModel, field_validator
from busapp.apputils.app_logger import applog

# ------------------------------------------------------
class Product(BaseModel):
    id: int    
    productName: str
    amountAvailable: int
    cost: int

    @field_validator('cost')
    @classmethod
    def cost_must_be_a_multiple_of_5_and_valid(cls, value:int) -> int:
        if value % 5 != 0:
            raise ValueError("Product cost must be a multiple of 5.")
    
        if value <= 0:
            raise ValueError("Product cost must be greater than 0.")
        
        if value >= 100000:
            raise ValueError("Product cost must be less than greater than 100000.")

        return value

    @field_validator('productName')
    @classmethod
    def productName_must_be_a_non_empty_string_or_more_than_128_chars(cls, productName:str) -> str:
        if len(productName) == 0:
            raise ValueError("productName must not be an empty string.")
    
        if len(productName) >= 128:
            raise ValueError("productName must not be longer than 128 characters.")

        return productName
    

    @field_validator('amountAvailable')
    @classmethod
    def amountAvailable_cannot_be_negative(cls, amountAvailable:int) -> int:
        if amountAvailable < 0:
            raise ValueError("amountAvailable cannot be negative.")
    
        machine_capacity_for_product_amount = 100 # TODO: put this to a config
        if amountAvailable > machine_capacity_for_product_amount:
            raise ValueError(f"amountAvailable cannot be more than the machine capacity of {machine_capacity_for_product_amount}")

        return amountAvailable
 