# E-Commerce Order Processing API - Cloud Pipeline

## 📌 Overview
An industry-grade E-Commerce Order Processing API deployed on AWS EC2 using Docker containerization, featuring SLA response metrics and automated failure recovery testing.

## 🚀 Cloud Infrastructure
- **Cloud Provider:** AWS (EC2 t3.micro / Ubuntu x86_64)
- **Containerization:** Docker
- **Framework:** Python FastAPI + Uvicorn
- **Live Endpoint:** `http://16.178.56.248`

## 📊 Measured Metrics
- **Availability Target (SLA):** 99.5%
- **Response Time Target:** < 200 ms
- **Measured Time to Recovery (TTR):** 15 Seconds

## ⚙️ How to Run Locally
1. Build Docker image:
   `docker build -t ecommerce-api .`
2. Run container:
   `docker run -d -p 8000:8000 ecommerce-api`
