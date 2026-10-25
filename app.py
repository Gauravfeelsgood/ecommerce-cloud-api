import os
import time
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="E-Commerce Order Processing API",
    description="Mini Project Industry Cloud Pipeline",
    version="1.0.0"
)

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrderRequest(BaseModel):
    customer_id: str
    item_id: str
    quantity: int
    amount: float

orders_db = []

@app.get("/")
def health_check():
    """Health Check Endpoint used for SLA & TTR monitoring"""
    return {
        "status": "HEALTHY",
        "service": "Order Processing API",
        "uptime": "100%"
    }

@app.post("/api/v1/orders")
def process_order(order: OrderRequest):
    """Processes customer orders and calculates response SLA latency"""
    start_time = time.time()
    
    if order.quantity <= 0 or order.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid order quantity or amount")
    
    order_data = {
        "order_id": f"ORD-{len(orders_db) + 1001}",
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

def terminate_process():
    """Helper function to kill the process after sending the crash HTTP response"""
    time.sleep(0.5)
    os._exit(1)

@app.post("/api/v1/crash")
def simulate_crash(background_tasks: BackgroundTasks):
    """Simulates an S1 Critical Failure by crashing the application server"""
    background_tasks.add_task(terminate_process)
    return {"message": "S1 Critical Crash initiated. Application process terminating..."}