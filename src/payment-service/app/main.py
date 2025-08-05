from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    amount: float
    currency: str
    recipient: str

@app.post("/payments")
async def create_payment(payment: Payment):
    return {"status": "success", "payment": payment}
