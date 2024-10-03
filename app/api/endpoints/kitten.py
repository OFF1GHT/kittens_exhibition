from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.crud.kitten import kitten_crud
from app.schemas.kitten import KittenCreate, KittenUpdate, KittenDB
from app.services.kitten import KittenService
from app.core.db import get_async_session

router = APIRouter()


# Создание котенка
@router.post("/kittens", response_model=KittenDB)
async def create_kitten(
    kitten_in: KittenCreate, session: AsyncSession = Depends(get_async_session)
):
    kitten_service = KittenService(session)
    kitten = await kitten_service.create_kitten(kitten_in)
    return kitten


# Получение всех котят
@router.get("/kittens", response_model=List[KittenDB])
async def get_kittens(session: AsyncSession = Depends(get_async_session)):
    kittens = await kitten_crud.get_all(session)
    return kittens


# Получение информации о котенке
@router.get("/kittens/{kitten_id}", response_model=KittenDB)
async def get_kitten_by_id(
    kitten_id: int, session: AsyncSession = Depends(get_async_session)
):
    kitten = await kitten_crud.get_kitten_by_id(kitten_id, session)
    if not kitten:
        raise HTTPException(status_code=404, detail="Котик не найден")
    return kitten


# Получение котиков определенной породы
@router.get("/kittens/breed/{breed_id}", response_model=List[KittenDB])
async def get_kittens_by_breed(
    breed_id: int, session: AsyncSession = Depends(get_async_session)
):
    kittens_query = await kitten_crud.get_kittens_by_breed(breed_id, session)
    if not kittens_query:
        raise HTTPException(status_code=404, detail="Не найдено котят с этой породой")

    return kittens_query


# Изменение информации о котенке
@router.put("/kittens/{kitten_id}", response_model=KittenDB)
async def update_kitten(
    kitten_id: int,
    kitten_in: KittenUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    update_kitten = await kitten_crud.update(kitten_id, kitten_in, session)
    if not update_kitten:
        raise HTTPException(
            status_code=404, detail="Невозможно обновить информацию о котике"
        )
    return update_kitten


# Удаление информации о котенке
@router.delete("/kittens/{kitten_id}", response_model=KittenDB)
async def delete_kitten(
    kitten_id: int, session: AsyncSession = Depends(get_async_session)
):
    kitten = await kitten_crud.get_kitten_by_id(kitten_id, session)
    if not kitten:
        raise HTTPException(status_code=404, detail="Котик не найден")
    await kitten_crud.remove(kitten, session)
    return kitten
