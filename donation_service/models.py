from sqlalchemy import Column, Integer, String
from database import Base

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String)
    amount = Column(Float)
