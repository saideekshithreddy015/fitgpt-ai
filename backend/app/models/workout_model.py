from sqlalchemy import Column, Integer, String, Float
from database import Base

class WorkoutLog(Base):
    __tablename__ = "workout_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    activity = Column(String)
    duration_minutes = Column(Integer)
    calories_burned = Column(Float)