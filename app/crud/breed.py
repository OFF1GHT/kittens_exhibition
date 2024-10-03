from app.crud.base import CRUDBase
from app.models.breed import Breed
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.models.breed import Breed
from sqlalchemy import select


class CRUDBreed(CRUDBase):
    async def get_breed_by_name(
        self,
        breed_name: str,
        session: AsyncSession,
    ) -> Optional[Breed]:
        result = await session.execute(select(Breed).where(Breed.name == breed_name))
        return result.scalars().first()


breed_crud = CRUDBreed(Breed)
