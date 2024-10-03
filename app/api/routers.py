from fastapi import APIRouter
from app.api.endpoints import kitten_router, breed_router

main_router = APIRouter()
main_router.include_router(
    breed_router,
    prefix="/breed",
    tags=["breeds"],
)
main_router.include_router(
    kitten_router,
    prefix="/kitten",
    tags=["kittens"],
)
