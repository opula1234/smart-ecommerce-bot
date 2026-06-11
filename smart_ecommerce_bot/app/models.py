from typing import Optional
from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    category: str
    brand: str
    price: float
    specs: str

    stock: int = Field(default=10)
