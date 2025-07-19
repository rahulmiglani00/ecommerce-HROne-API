from typing import List, Optional

class ProductResponse:
    def __init__(self, _id, name, price):
        self.id = str(_id)
        self.name = name
        self.price = price

class OrderItemResponse:
    def __init__(self, product_details, qty):
        self.productDetails = product_details
        self.qty = qty

class OrderResponse:
    def __init__(self, _id, items, total):
        self.id = str(_id)
        self.items = items
        self.total = total
