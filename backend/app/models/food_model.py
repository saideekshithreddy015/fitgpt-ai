from sqlalchemy import Column, Integer, String, Float
from database import Base

class FoodLog(Base):
    __tablename__ = "food_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    food_name = Column(String)
    quantity = Column(Float)
    calories = Column(Float)
    protein = Column(Float)