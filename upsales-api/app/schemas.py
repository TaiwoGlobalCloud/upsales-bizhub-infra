from pydantic import BaseModel, EmailStr, Field


class CustomerBase(BaseModel):
    name: str = Field(
        example="Michael Brown"
    )
    email: EmailStr = Field(
        example="michael.brown@upsalesbizhub.com"
    )
    company: str = Field(
        example="UpSales BizHub"
    )


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True