from fastapi import APIRouter, Depends

from app.dependencies.auth_dependency import get_current_user
from app.dependencies.db_dependency import get_db
from app.schemas.auth_schemas import CurrentUser
from app.schemas.expense_schemas import ExpenseResponse, ExpenseSchema, ExpenseUpdate
from app.services import expense_service

router = APIRouter()


@router.post("/expenses", response_model=ExpenseResponse)
def create_expense(
    data: ExpenseSchema,
    current_user: CurrentUser = Depends(get_current_user),
    db=Depends(get_db),
):
    return expense_service.create_expense(data, current_user, db)


@router.get("expenses", response_model=list[ExpenseResponse])
def get_all_expenses(
    current_user: CurrentUser = Depends(get_current_user), db=Depends(get_db)
):
    return expense_service.get_all_expenses_of_user(current_user, db)


@router.put("expenses/{id}", response_model=ExpenseResponse)
def update_expense(
    id: int,
    data: ExpenseUpdate,
    current_user: CurrentUser = Depends(get_current_user),
    db=Depends(get_db),
):
    return expense_service.update_expense(id, data, current_user, db)


@router.delete("expenses/{id}", status_code=204)
def delete_expense(
    id: int, current_user: CurrentUser = Depends(get_current_user), db=Depends(get_db)
):
    return expense_service.delete_expense(id, current_user, db)
