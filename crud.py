from bson import ObjectId
from database import products_collection, orders_collection
from models import ProductModel, OrderModel
from schemas import ProductResponse, OrderItemResponse, OrderResponse
from pymongo import ASCENDING

async def create_product(data: ProductModel):
    result = await products_collection.insert_one(data.dict())
    return str(result.inserted_id)

async def get_products(name=None, size=None, limit=10, offset=0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = products_collection.find(query).sort("_id", ASCENDING).skip(offset).limit(limit)
    products = []
    async for product in cursor:
        products.append(ProductResponse(product["_id"], product["name"], product["price"]).__dict__)

    return products, offset + limit, offset - limit

async def create_order(data: OrderModel):
    total = 0
    product_details = []

    for item in data.items:
        product = await products_collection.find_one({"_id": ObjectId(item.productId)})
        if not product:
            continue
        total += item.qty * product["price"]
        product_details.append({
            "productId": item.productId,
            "qty": item.qty
        })

    order = {
        "userId": data.userId,
        "items": product_details,
        "total": total
    }

    result = await orders_collection.insert_one(order)
    return str(result.inserted_id)

async def get_orders(user_id, limit=10, offset=0):
    cursor = orders_collection.find({"userId": user_id}).sort("_id", ASCENDING).skip(offset).limit(limit)
    orders = []

    async for order in cursor:
        item_details = []
        for item in order["items"]:
            product = await products_collection.find_one({"_id": ObjectId(item["productId"])})
            if product:
                product_info = {"name": product["name"], "id": str(product["_id"])}
                item_details.append(OrderItemResponse(product_info, item["qty"]).__dict__)
        orders.append(OrderResponse(order["_id"], item_details, order["total"]).__dict__)

    return orders, offset + limit, offset - limit
