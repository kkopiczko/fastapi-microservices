from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import random
import schemas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

inventory = []

@app.get('/products')
def get_products():
    return inventory

@app.get('/products/{product_id}')
def get_product(product_id: int):
    product = None
    for p in inventory:
        if p['id'] == product_id:
            product = p
            break
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with id: {product_id} was not found in the inventory')

    return product

@app.post('/products')
def create_product(product: schemas.Product):
    product = product.dict()
    product['id'] = random.randint(1, 10000)
    print(product)
    inventory.append(product)
    return product

