from pydantic import BaseModel, Field
from typing import List

class SizeModel(BaseModel):
    size: str
    quantity: int

class ProductModel(BaseModel):
    name: str
    price: float
    sizes: List[SizeModel]

class OrderItemModel(BaseModel):
    productId: str
    qty: int

class OrderModel(BaseModel):
    userId: str
    items: List[OrderItemModel]
