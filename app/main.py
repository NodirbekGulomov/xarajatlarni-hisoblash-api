from fastapi import FastAPI

from app.routers.auth_router import router as auth_router
from app.routers.expense_router import router as expense_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(expense_router)
