from fastapi import APIRouter

from busapp.apputils.app_logger import applog

from busapp.services.crud_service import CRUDService
from busapp.services.models.product import ProductWoID, Product
from typing import List

# ------------------------------------------------------

crud_service_product = CRUDService[Product](Product)
router_products = APIRouter()

# ------------------------------------------------------

@router_products.post("/products/", response_model=Product)
async def create_product(product: ProductWoID):
    return crud_service_product.create(product)

@router_products.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    return crud_service_product.get(product_id)

@router_products.get("/products/", response_model=List[ProductWoID])
async def get_products():
    return crud_service_product.get_all()

@router_products.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product):
    return crud_service_product.update(product_id, updated_product)

@router_products.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    return crud_service_product.delete(product_id)