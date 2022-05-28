from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import requests
import schemas as _schemas
from typing import List

app = FastAPI()

orders=[]

@app.get('/orders', response_model=List[_schemas.Order])
def get_orders():
    return orders

@app.post('/orders')
async def create_order(request: Request): #id, quantity
    body = await request.json()
    r = requests.get('http://localhost:8000/products/%s' % body['product_id'])
    
    if r.status_code == 404:
        return r.json()
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
    return prod