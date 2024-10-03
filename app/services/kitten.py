from fastapi import HTTPException
from app.crud.kitten import kitten_crud
from app.crud.breed import breed_crud
from app.schemas.kitten import KittenCreate, KittenDB


class KittenService:
    def __init__(self, session):
        self.session = session

    async def create_kitten(self, kitten_in: KittenCreate) -> KittenDB:
        breed = await breed_crud.get(kitten_in.breed_id, self.session)
        if not breed:
            raise HTTPException(status_code=500, detail="Порода не найдена")
        kitten = await kitten_crud.create(kitten_in, self.session)
        return kitten
