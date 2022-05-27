from pydantic import BaseModel

class OrderCreate(BaseModel):
    id: int
    quantity: int

class Order(BaseModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str #pending, completed, refunded

