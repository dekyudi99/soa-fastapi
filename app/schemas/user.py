from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id_users: int
    username: str

    class Config:
        orm_mode = True
