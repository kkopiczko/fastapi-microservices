from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import requests
import schemas as _schemas

app = FastAPI()

orders=[]

@app.post('/orders')
async def create_order(request: Request): #id, quantity
    body = await request.json()
    r = requests.get('http://localhost:8000/products/%s' % body['product_id'])
    prod = r.json()

    order = _schemas.Order(
        product_id=body['product_id'],
        price=prod['price'],
        fee=0.2*prod['price'],
        total=1.2*prod['price'],
        quantity=body['quantity'],
        status='pending'
    )
    orders.append(order)
    return order