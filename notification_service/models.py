from sqlalchemy import Column, Integer, String
from database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, index=True)
    task_title = Column(String)
