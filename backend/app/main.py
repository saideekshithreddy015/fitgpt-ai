from fastapi import FastAPI
from database import engine, Base
from models import user_model
from models import workout_model
from models import food_model
from models import chat_model

from routers import user_router

from routers import workout_router
from routers import chat_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FitGPT AI")

app.include_router(user_router.router)
app.include_router(workout_router.router)
app.include_router(chat_router.router)

@app.get("/")
def home():
    return {"message": "FitGPT AI Backend Running"}