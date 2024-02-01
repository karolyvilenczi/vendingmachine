from fastapi import APIRouter, Depends

from busapp.apputils.app_logger import applog

from busapp.services.crud_service import ProdCRUDService
from busapp.services.models.product import Product, ProductResponse
from typing import List, Optional

from busapp.services.vending_machine import (
    VendingMachine, States
)
# ------------------------------------------------------

global vm
vm = VendingMachine()


crud_service_product = ProdCRUDService(Product)
router_products = APIRouter(prefix="/products")


async def is_machine_in_maintenance():
    if vm.state is States.MAINTENANCE:
        applog.debug("Machine is in maintennance")
        return True
    else:
        # applog.warning("Machine is not ready, cannot perform requested operation.")
        return False

async def is_machine_selling():
    if vm.state is States.SELLING:
        applog.debug("Machine is selling")
        return True
    else:
        # applog.warning("Machine is not in state selling, cannot perform operation.")
        return False

# async def is_machine_ready_or_selling():
#     return True if await is_machine_ready() or await is_machine_selling() else False
       
# ------------------------------------------------------

@router_products.get("/stats/")
async def get_count_of(in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:
        return crud_service_product.get_count_of(sum_field_name="amount")
    else:
        return{"error":"Machine not in maintenance."}



@router_products.get("/stats/{product_name}")
async def get_count_of(product_name:Optional[str]=""):
    return crud_service_product.get_count_of(        
        product_name=product_name,        
        sum_field_name="amount"
    )

@router_products.get("/detail/{product_id}", response_model=ProductResponse)
async def get_product(product_id: Optional[int]):
    return crud_service_product.get(product_id)


@router_products.get("/", response_model=List[ProductResponse])
async def get_products():
    return crud_service_product.get_all()


@router_products.post("/", response_model=ProductResponse)
async def create_product(product: Product, in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:
        return crud_service_product.create(product)
    else:
        return{"error":"Machine not in maintenance."}

@router_products.post("/save")
async def save_products_to_machine(in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:        
        current_products = crud_service_product.get_all() # TODO: here I need the stats
        vm.inventory = current_products
    else:
        return{"error":"User operations can only be performed in maintenance mode."}

@router_products.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product, in_maintenance: bool = Depends(is_machine_in_maintenance)):
    if in_maintenance:
        return crud_service_product.update(product_id, updated_product)
    else:
        return{"error":"Machine not in maintenance."}
    

@router_products.delete("/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    return crud_service_product.delete(product_id)

