from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class ExpenseSchema(BaseModel):
    name: str
    amount: Decimal
    category: str


class ExpenseResponse(BaseModel):
    id: int
    name: str
    amount: Decimal
    category: str


class ExpenseUpdate(BaseModel):
    id: int
    name: str
    amount: Decimal
    category: str
    date: date
    user_id: int
