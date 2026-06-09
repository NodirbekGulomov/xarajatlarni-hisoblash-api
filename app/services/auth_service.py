from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.db.models import User
from app.schemas.auth_schemas import LoginSchema, RegisterSchema


def create_user(data: RegisterSchema, db: Session):
    user = db.execute(select(User).where(User.email == data.email)).scalar_one_or_none()
    if user:
        raise HTTPException(status_code=409, detail="Email already exists")
    data = data.model_dump(exclude_none=True)
    data["hashed_password"] = hash_password(data.pop("password"))
    db_user = User(**data)
    db.add(db_user)
    db.commit()
    access_token_data = {"id": db_user.id}
    return {
        "access_token": create_access_token(access_token_data),
        "refresh_token": create_refresh_token(db_user.id),
    }


def handle_login(data: LoginSchema, db: Session):
    user = db.execute(select(User).where(User.email == data.email)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=401, detail="Email or password is not correct")
    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Email or password is not correct")

    access_token_data = {"id": user.id}
    return {
        "access_token": create_access_token(access_token_data),
        "refresh_token": create_refresh_token(user.id),
    }
