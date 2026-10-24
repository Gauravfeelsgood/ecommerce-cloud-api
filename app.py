import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="E-Commerce Order Processing API",
    description="Mini Project Industry Cloud Pipeline",
    version="1.0.0"
)

class OrderRequest(BaseModel):
    customer_id: str
    item_id: str
    quantity: int
    amount: float

# In-memory storage for orders
orders_db = []

@app.get("/")
def health_check():
    """Health Check Endpoint for AWS Load Balancer / Monitoring"""
    return {
        "status": "HEALTHY",
        "service": "Order Processing API",
        "uptime": "100%"
    }

@app.post("/api/v1/orders")
def process_order(order: OrderRequest):
    """Processes incoming customer orders (SLA Target: < 200ms)"""
    start_time = time.time()
    
    if order.quantity <= 0 or order.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid order quantity or amount")
    
    order_id = f"ORD-{len(orders_db) + 1001}"
    order_data = {
        "order_id": order_id,
        "customer_id": order.customer_id,
        "item_id": order.item_id,
        "quantity": order.quantity,
        "amount": order.amount,
        "status": "PROCESSED"
    }
    
    orders_db.append(order_data)
    elapsed_time_ms = (time.time() - start_time) * 1000
    
    return {
        "message": "Order processed successfully",
        "order": order_data,
        "response_time_ms": round(elapsed_time_ms, 2)
    }