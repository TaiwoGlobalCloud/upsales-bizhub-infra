from fastapi import FastAPI
from app.routers import customers
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="UpSales BizHub API",
    version="1.0.0"
)

app.include_router(customers.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to UpSales BizHub API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }