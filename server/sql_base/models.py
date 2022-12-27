from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = None

class User(BaseModelModify):
    login: str
    password: str

class Personal(User):
    power_level: int = 1

class Conference(BaseModelModify):
    name: str
    place: str
    presonalId: int



