from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.db import Expense
from app.schemas.expense_schemas import ExpenseSchema


def create_expense(data: ExpenseSchema, user_id: int, db: Session):
    data["user_id"] = user_id
    expense = Expense(**data.model_dump())
    db.add(expense)
    db.commit()
    return expense


def get_all_expenses_of_user(user_id: int, db: Session):
    expenses = db.execute(select(Expense).where(Expense.user_id == user_id)).scalars()
    return expenses


def update_expense(expense_id: int, data: ExpenseSchema, user_id: int, db: Session):
    expense = db.execute(
        select(Expense).where(Expense.id == expense_id)
    ).scalar_one_or_none()

    if expense is None:
        raise HTTPException(status_code=404)

    if expense.user_id != user_id:
        raise HTTPException(status_code=0)

    db_expense = Expense(**data.model_dump())
    db.add(db)
    db.commit()
    return db_expense


def delete_expense(expense_id, user_id: int, db: Session):
    expense = db.execute(
        select(Expense).where(Expense.id == expense_id)
    ).scalar_one_or_none()

    if expense is None:
        raise HTTPException(status_code=404)

    if expense.user_id != user_id:
        raise HTTPException(status_code=0)

    db.execute(delete(Expense).where(Expense.id == expense_id))
    db.commit()
    return expense
