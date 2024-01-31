from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from collections import Counter
from pandas import DataFrame 
from typing import Type, List, Dict, Optional, TypeVar, Generic

# from busapp.services.models.product import ProductWoID, Product

from busapp.apputils.app_logger import applog

ModelType = TypeVar("ModelType", bound=BaseModel)

class CRUDService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        
        self.database = list()        
        # self.inventory:List[Dict] = list()
        self.current_id = 1        
        

    def create(self, item: ModelType):
        item_dict = jsonable_encoder(item)
        item_dict["id"] = self.current_id
        self.current_id += 1
        created_item = self.model(**item_dict)
        self.database.append(created_item)        
        
        return created_item

    def get(self, item_id: int) -> ModelType:
        item = next((i for i in self.database if i.id == item_id), None)
        if item:
            return item
        else:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")

    def get_all(self) -> List[ModelType]:
        return self.database
    
    def get_count_of(
            self, 
            key_name:str, 
            value_name:str = "",
            sum_field_name:str = ""
            ) -> List[Dict]:
        # e.g. for product: get count of productName or sellerid        
        # e.g. for user: get count of role buyer
        
        items_w_key_name_found = [dict(item) for item in self.database if (key_name in item.__annotations__)]
        items_df = DataFrame(items_w_key_name_found)

        # Count occurrences of each product
        iten_counts = items_df[key_name].value_counts().to_dict()

        # Sum 'amount' values for each product
        items_sums_by_a_different_field = items_df.groupby(key_name)[sum_field_name].sum().to_dict()      
        
        
        return(items_sums_by_a_different_field)
        
    
    def get_database_in_dict(self) -> List[ModelType]:
        return [item.model_dump() for item in self.database]
        

    def update(self, item_id: int, updated_item: ModelType) -> ModelType:
        item = next((i for i in self.database if i.id == item_id), None)
        if item:
            jsonable_item = jsonable_encoder(updated_item)
            for field in jsonable_item:
                setattr(item, field, jsonable_item[field])
            return item
        else:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")

    def delete(self, item_id: int) -> ModelType:
        item = next((i for i in self.database if i.id == item_id), None)
        if item:
            self.database.remove(item)
            return item
        else:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")