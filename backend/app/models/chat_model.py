from sqlalchemy import Column, Integer, String
from database import Base

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    role = Column(String)
    message = Column(String)