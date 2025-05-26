from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import logging

from database import Base, engine, get_db
import models
from schemas import DonationCreate

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
logging.basicConfig(level=logging.INFO)

@app.post("/donate")
def process_donation(donation: DonationCreate, db: Session = Depends(get_db)):
    db_donation = models.Donation(user_email=donation.user_email, amount=donation.amount)
    db.add(db_donation)
    db.commit()
    db.refresh(db_donation)

    logging.info(f"💸 Processed {donation.amount}€ donation from {donation.user_email}")
    return {"status": "ok", "message": "Donation processed"}


