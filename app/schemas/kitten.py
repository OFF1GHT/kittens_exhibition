from pydantic import BaseModel
from typing import Optional


class KittenBase(BaseModel):
    name: str
    color: str
    age_in_months: int
    description: Optional[str] = None


class KittenCreate(KittenBase):
    breed_id: int


class KittenUpdate(KittenBase):
    breed_id: int


class KittenDB(KittenBase):
    id: int

    class Config:
        orm_mode = True
