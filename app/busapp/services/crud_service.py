from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Type, List, TypeVar, Generic

from busapp.apputils.app_logger import applog


ModelType = TypeVar("ModelType", bound=BaseModel)

class CRUDService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.database = []
        self.current_id = 1  # Initial ID value

    def create(self, item: ModelType):
        item_dict = jsonable_encoder(item)
        item_dict["id"] = self.current_id
        self.current_id += 1
        created_item = self.model(**item_dict)
        self.database.append(created_item)

        applog.debug(created_item)
        return created_item

    def get(self, item_id: int) -> ModelType:
        item = next((i for i in self.database if i.id == item_id), None)
        if item:
            return item
        else:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")

    def get_all(self) -> List[ModelType]:
        return self.database

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
