from fastapi import APIRouter
from services.helloworldServices import *
router = APIRouter()

@router.get("/")
def hello_world():
    return hello_world_service()

@router.get("/{name}")
def hello_world_with_name(name: str):
    return hello_world_with_name_service(name)
