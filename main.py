from fastapi import FastAPI, Query
from models import ProductModel, OrderModel
from crud import create_product, get_products, create_order, get_orders
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Product
@app.post("/products", status_code=201)
async def add_product(product: ProductModel):
    product_id = await create_product(product)
    return {"id": product_id}

# List Products
@app.get("/products", status_code=200)
async def list_products(
    name: str = None,
    size: str = None,
    limit: int = Query(10),
    offset: int = Query(0)
):
    products, next_offset, prev_offset = await get_products(name, size, limit, offset)
    return {
        "data": products,
        "page": {
            "next": str(next_offset),
            "limit": limit,
            "previous": str(prev_offset)
        }
    }

# Create Order
@app.post("/orders", status_code=201)
async def add_order(order: OrderModel):
    order_id = await create_order(order)
    return {"id": order_id}

# List Orders by user
@app.get("/orders/{user_id}", status_code=200)
async def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders, next_offset, prev_offset = await get_orders(user_id, limit, offset)
    return {
        "data": orders,
        "page": {
            "next": str(next_offset),
            "limit": limit,
            "previous": str(prev_offset)
        }
    }
