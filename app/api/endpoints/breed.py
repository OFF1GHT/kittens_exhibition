from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.breed import breed_crud
from app.schemas.breed import BreedCreate, BreedDB
from app.core.db import get_async_session
from app.services.breed import BreedService
from typing import List

router = APIRouter()


# Создание породы
@router.post("/breeds", response_model=BreedDB)
async def create_breed(
    breed_in: BreedCreate, session: AsyncSession = Depends(get_async_session)
):
    breed_service = BreedService(session)
    breed = await breed_service.create_product(breed_in)
    return breed


# Получение всех пород
@router.get("/breeds", response_model=List[BreedDB])
async def get_breeds(session: AsyncSession = Depends(get_async_session)):
    breeds = await breed_crud.get_all(session)
    return breeds
