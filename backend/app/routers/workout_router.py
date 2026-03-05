from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.workout_model import WorkoutLog
from services.workout_engine import predict_calories

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log-workout")
def log_workout(user_id: int, activity: str, duration_minutes: int, weight: float, db: Session = Depends(get_db)):

    calories = predict_calories(weight, activity, duration_minutes)

    workout = WorkoutLog(
        user_id=user_id,
        activity=activity,
        duration_minutes=duration_minutes,
        calories_burned=calories
    )

    db.add(workout)
    db.commit()
    db.refresh(workout)

    return {
        "message": "Workout logged",
        "activity": activity,
        "duration": duration_minutes,
        "calories_burned": calories
    }