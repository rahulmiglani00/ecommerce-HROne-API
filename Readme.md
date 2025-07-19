# FastAPI Products App

A simple FastAPI application for managing products and orders with MongoDB.

## Features

- Add and list products with sizes and prices
- Create and list orders for users
- Pagination support for listing endpoints
- MongoDB backend (async with Motor)

## Project Structure

```
fastapi-products-app/
│
├── .env                # Environment variables (MongoDB URI)
├── crud.py             # CRUD operations for products and orders
├── database.py         # MongoDB connection and collections
├── main.py             # FastAPI app and API routes
├── models.py           # Pydantic models for request validation
├── schemas.py          # Response schemas
├── requirements.txt    # Python dependencies
└── Readme.md           # Project documentation
```

## Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/rahulmiglani00/fastapi-products-app.git
    cd fastapi-products-app

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment**
   - Set your MongoDB URI in the `.env` file:
     ```
     MONGO_URI=your_mongodb_connection_string
     ```

4. **Run the application**
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

### Products

- **Create Product**
  - `POST /products`
  - Request body:  
    ```json
    {
      "name": "T-Shirt",
      "price": 19.99,
      "sizes": [
        {"size": "M", "quantity": 10},
        {"size": "L", "quantity": 5}
      ]
    }
    ```
  - Response:  
    ```json
    {"id": "<product_id>"}
    ```

- **List Products**
  - `GET /products?name=<name>&size=<size>&limit=<limit>&offset=<offset>`
  - Response:  
    ```json
    {
      "data": [ ...products... ],
      "page": {
        "next": "<next_offset>",
        "limit": 10,
        "previous": "<prev_offset>"
      }
    }
    ```

### Orders

- **Create Order**
  - `POST /orders`
  - Request body:  
    ```json
    {
      "userId": "user123",
      "items": [
        {"productId": "<product_id>", "qty": 2}
      ]
    }
    ```
  - Response:  
    ```json
    {"id": "<order_id>"}
    ```

- **List Orders by User**
  - `GET /orders/{user_id}?limit=<limit>&offset=<offset>`
  - Response:  
    ```json
    {
      "data": [ ...orders... ],
      "page": {
        "next": "<next_offset>",
        "limit": 10,
        "previous": "<prev_offset>"
      }
    }
    ```

## Code Overview

- [`main.py`](main.py): FastAPI app, API routes, and CORS setup.
- [`models.py`](models.py): Pydantic models for product and order requests.
- [`schemas.py`](schemas.py): Response schemas for products and orders.
- [`crud.py`](crud.py): Async CRUD operations for MongoDB.
- [`database.py`](database.py): MongoDB connection and collection setup.

## Dependencies

See [requirements.txt](requirements.txt):

- fastapi
- uvicorn
- pydantic
- pymongo
- python-dotenv

## Author Rahul Miglani


