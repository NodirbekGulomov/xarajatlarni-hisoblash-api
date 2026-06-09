from pydantic import BaseModel


class UserProfileResponse(BaseModel):
    id: int
    name: str
    email: str
