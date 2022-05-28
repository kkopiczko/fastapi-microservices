from pydantic import BaseModel

class OrderBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    price: float
    fee: float
    total: float
    status: str #pending, completed, refunded

