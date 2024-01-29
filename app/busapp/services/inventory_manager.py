"""
Module to implement the inventory management functions
"""
from dataclasses import dataclass
from pydantic import BaseModel, field_validator
from typing import List

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

      

class Inventory:
    def __init__(self):
        self.product_list = []
        applog.info("New empty inventory created.")

    def add_product(self, product:Product):
        self.product_list.append(product)

    def get_product_by_id(self, id:int):
        filtered = list(filter(lambda product: product.id == id, self.product_list))
        return filtered
    
    def delete_product_by_id(self, product_id:int):
        return [product for product in self.product_list if product.id != product_id]
    
    def delete_product_by_id(self, product_id:int):
        return [product for product in self.product_list if product.id != product_id]
    
    def update_product_by_id(self, product_id, new_product_name, new_amount_available, new_cost):
        product_to_update = self.get_product_by_id(product_id)
        product_to_update.productName = new_product_name
        product_to_update.amountAvailable = new_amount_available
        product_to_update.cost = new_cost
        # TODO: does it really udpate it? pass by ref?
    
        


# TODO: add tests



    # def add_item(self, item: Item):
    #     self.items.append(item)

    # def get_item(self, item_id: int) -> Item:
    #     # TODO: to list compr
    #     for item in self.items:
    #         if item.id == item_id:
    #             return item
    #     # TODO: custom exception item not found
    #     # raise HTTPException(status_code=404, detail="Item not found")
    #     raise Exception("Item not found")

    # def get_all_items(self) -> List:
    #     return self.items

    # def get_inventory_length(self) -> int:
    #     inventory_length = self.get_all_items()
    #     return len(inventory_length)

# TODO: add tests
        




# class MachineRow(BaseModel):
#     id:int
#     position: tuple
#     size: int

#     def __init__(self, id, position, size):
#         self.id = id
#         self.position = position
#         self.size = size

#     def __str__(self):
#         return f"Machine row id: {self.id} with size {self.size} possible items."

#     def rotate(self):
#         applog.info(f"Rotating spring id {self.id} at position: {self.position}.")


# class ItemRow(MachineRow):
#     name: str
#     occupancy: int

#     def __init__(self, name, occupancy):
#         self.name = name
#         self.occupancy = occupancy

#     def __str__(self):
#         return f"Itemrow of {self.name} filled {self.occupancy} of {super().size}"