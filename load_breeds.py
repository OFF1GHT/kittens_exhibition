import asyncio
import csv
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.breed import Breed
from app.core.db import get_async_session
from sqlalchemy import select

CSV_FILE_PATH = "breeds.csv"


async def load_breeds_from_csv():
    # Получаем сессию
    async for session in get_async_session():
        await add_breeds_from_csv(session)


async def add_breeds_from_csv(session: AsyncSession):
    with open(CSV_FILE_PATH, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            breed_name = row["name"]
            existing_breed = await session.execute(
                select(Breed).where(Breed.name == breed_name)
            )
            if not existing_breed.scalars().first():
                db_breed = Breed(name=breed_name)
                session.add(db_breed)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(load_breeds_from_csv())
