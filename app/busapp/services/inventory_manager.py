"""
Module to implement the inventory management functions
"""

from pydantic import BaseModel
from typing import List

from busapp.apputils import app_logger

# ------------------------------------------------------
applog = app_logger.make_logger("SRV:INVENTORY MANAGER")


class Item(BaseModel):
    id: int    
    name: str
    price: float


class MachineRow(BaseModel):
    id:int
    position: tuple
    size: int

    def __init__(self, id, position, size):
        self.id = id
        self.position = position
        self.size = size

    def __str__(self):
        return f"Machine row id: {self.id} with size {self.size} possible items."

    def rotate(self):
        applog.info(f"Rotating spring id {self.id} at position: {self.position}.")


class ItemRow(MachineRow):
    name: str
    occupancy: int

    def __init__(self, name, occupancy):
        self.name = name
        self.occupancy = occupancy

    def __str__(self):
        return f"Itemrow of {self.name} filled {self.occupancy} of {super().size}"



class Inventory:
    def __init__(self):
        self.items = []
        applog.info("New inventory created.")

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