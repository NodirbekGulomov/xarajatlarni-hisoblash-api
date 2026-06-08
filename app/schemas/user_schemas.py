from pydantic import BaseModel


class UserProfileSchema(BaseModel):
    id: int
    name: str
    email: str
