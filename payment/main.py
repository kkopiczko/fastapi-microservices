from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import requests
import schemas as _schemas

app = FastAPI()

@app.post('/orders')
async def create_order(request: Request): #id, quantity
    print('POST order request')
    body = await request.json()
    print(body['id'])
    r = requests.get('http://localhost:8000/products/%s' % body['id'])
    prod = r.json()

    return 