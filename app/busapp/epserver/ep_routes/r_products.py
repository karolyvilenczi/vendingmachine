from fastapi import APIRouter

from busapp.apputils.app_logger import applog

from busapp.services.crud_service import CRUDService
from busapp.services.models.product import Product, ProductResponse
from typing import List, Optional

# ------------------------------------------------------

crud_service_product = CRUDService[Product](Product)
router_products = APIRouter(prefix="/products")

# ------------------------------------------------------

@router_products.get("/stats/")
async def get_count_of():
    return crud_service_product.get_count_of(key_name="productName", sum_field_name="amount")

@router_products.get("/stats/{product_name}")
async def get_count_of(product_name:Optional[str]=""):
    return crud_service_product.get_count_of(key_name="productName", value_name=product_name)

@router_products.get("/detail/{product_id}", response_model=ProductResponse)
async def get_product(product_id: Optional[int]):
    return crud_service_product.get(product_id)


@router_products.get("/", response_model=List[ProductResponse])
async def get_products():
    return crud_service_product.get_all()


@router_products.post("/", response_model=ProductResponse)
async def create_product(product: Product):
    return crud_service_product.create(product)


@router_products.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product):
    return crud_service_product.update(product_id, updated_product)

@router_products.delete("/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    return crud_service_product.delete(product_id)

