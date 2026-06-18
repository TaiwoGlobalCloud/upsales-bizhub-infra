from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/")
def get_customers(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(models.Customer).all()


@router.get("/{customer_id}")
def get_customer(
    customer_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    customer = db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.post("/")
def create_customer(
    customer: schemas.CustomerCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        company=customer.company
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


@router.put("/{customer_id}")
def update_customer(
    customer_id: int,
    customer: schemas.CustomerCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_customer = db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()

    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db_customer.name = customer.name
    db_customer.email = customer.email
    db_customer.company = customer.company

    db.commit()
    db.refresh(db_customer)

    return db_customer


@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Admin-only authorization
    if current_user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Admin privileges required"
        )

    customer = db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully"
    }