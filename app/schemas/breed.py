from pydantic import BaseModel


class BreedBase(BaseModel):
    name: str


class BreedCreate(BreedBase):
    pass


class BreedDB(BreedBase):
    id: int

    class Config:
        orm_mode = True
