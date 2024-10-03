import csv
import asyncio
from app.core.db import get_async_session
from app.models.kitten import Kitten


async def load_kittens_from_csv(file_path: str):
    async for session in get_async_session():
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Обрабатываем котенка: {row}")
                if "breed_id" not in row:
                    print("Ошибка: 'breed_id' не найден в строке")
                    continue
                kitten = Kitten(
                    name=row["name"],
                    color=row["color"],
                    age_in_months=int(row["age_in_months"]),
                    description=row["description"],
                    breed_id=int(row["breed_id"]),
                )
                session.add(kitten)
            await session.commit()


if __name__ == "__main__":
    asyncio.run(load_kittens_from_csv("kittens.csv"))
