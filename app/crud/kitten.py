from app.crud.base import CRUDBase
from app.models.kitten import Kitten
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy import select
from typing import List


class CRUDKitten(CRUDBase):
    async def get_kitten_by_id(
        self, kitten_id, session: AsyncSession
    ) -> Optional[Kitten]:
        result = await session.execute(select(Kitten).where(Kitten.id == kitten_id))
        return result.scalars().first()

    async def get_kittens_by_breed(
        self, breed_id: int, session: AsyncSession
    ) -> List[Kitten]:
        result = await session.execute(
            select(Kitten).where(Kitten.breed_id == breed_id)
        )
        return result.scalars().all()


kitten_crud = CRUDKitten(Kitten)
