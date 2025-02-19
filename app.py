from fastapi import FastAPI, APIRouter
from api.helloworld import router as helloworld_router
from core.config import settings
import logfire
import os

app = FastAPI()

# Modify the logfire configuration to use token directly from settings
logfire.configure(token=os.environ.get("LOGFIRE_TOKEN"))
logfire.instrument_fastapi(app, capture_headers=True)

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(helloworld_router, tags=["Hello World"], prefix="/api")
