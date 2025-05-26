from pydantic import BaseModel

class DonationCreate(BaseModel):
    user_email: str
    amount: float
