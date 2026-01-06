from sqlalchemy import Column, Integer, String
from .database import Base

class UserActivity(Base):
    __tablename__ = "user_activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    action = Column(String)
