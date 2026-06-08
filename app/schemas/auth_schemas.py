from pydantic import BaseModel


class CurrentUser(BaseModel):
    id: int


class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str


class LoginSchema(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
