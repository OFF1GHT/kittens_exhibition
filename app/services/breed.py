from fastapi import HTTPException
from app.crud.breed import breed_crud
from app.schemas.breed import BreedCreate


class BreedService:
    def __init__(self, session):
        self.session = session

    async def _check_name_duplicate(self, breed_name: str) -> None:
        breed = await breed_crud.get_breed_by_name(breed_name, self.session)
        if breed is not None:
            raise HTTPException(
                status_code=400, detail="Порода с таким названием уже существует."
            )

    async def create_product(self, breed: BreedCreate):
        await self._check_name_duplicate(breed.name)
        new_breed = await breed_crud.create(breed, self.session)
        return new_breed
