from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from collections import Counter
from pandas import DataFrame 
from typing import Type, List, Dict, Optional, TypeVar, Generic


from busapp.services.models.product import Product
from busapp.services.models.user import User
from busapp.services.models.money import Coin


from busapp.apputils.app_logger import applog

ModelType = TypeVar("ModelType", bound=BaseModel)

class CRUDService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.database = list()        
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
        
    def delete_all(self) -> bool:
        """
            Resets the database to an empty list
        """
        self.database = []
        return True
        


class ProdCRUDService(CRUDService[Product]):

    def __init__(self, model: type[Product]):
        super().__init__(model)
    
    def get_count_of(self, product_name:str="", sum_field_name:str="") -> List[Dict]:
        # e.g. for product: get count of productName or sellerid        
        # e.g. for user: get count of role buyer
  
        products = [dict(item) for item in self.database if ("productName" in item.__annotations__)]
        products_df = DataFrame(products)
       
        items_sums = products_df.groupby("productName")[sum_field_name].sum().to_dict()      
        if product_name:
            return items_sums.get(product_name, 0)
        
        return(items_sums)
    

class UserCRUDService(CRUDService[User]):
    
    def __init__(self, model: type[User]):
        super().__init__(model)

    


class MoneyCRUDService(CRUDService[Coin]):

    def __init__(self, model: type[Coin]):
        super().__init__(model)

    def get_all(self):
        return super().get_all()
    
    def get_sum(self):
        applog.debug("getting sum entered")

        coins_from_db_as_dicts = [dict(coin) for coin in self.database]
        coins_df = DataFrame(coins_from_db_as_dicts)
       
        entered_coins_sum = int(coins_df["face_value"].sum())
        
        resp = {
            'entered_sum':entered_coins_sum
        }      
       
        return(resp)
    
    def delete_all(self):        
        resp = {
            "Sum cleared":super().delete_all()
        }
        return resp
       