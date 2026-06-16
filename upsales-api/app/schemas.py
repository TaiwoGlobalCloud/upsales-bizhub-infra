from pydantic import BaseModel, EmailStr, Field


# Customer Schemas
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


# User Schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str