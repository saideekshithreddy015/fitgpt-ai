from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user_model import User

router = APIRouter()

# database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create-user")
def create_user(name: str, age: int, gender: str, height: float, weight: float, goal: str, db: Session = Depends(get_db)):

    new_user = User(
        name=name,
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        goal=goal
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created", "user_id": new_user.id}