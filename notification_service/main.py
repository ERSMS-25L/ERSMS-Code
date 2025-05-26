from fastapi import FastAPI, Depends
from pydantic import BaseModel
import logging
from sqlalchemy.orm import Session
import models, database, schemas

from database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
logging.basicConfig(level=logging.INFO)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notify")
def notify(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    logging.info(f"📧 Sent email to {notification.user_email} for task: {notification.task_title}")
    db_notif = models.Notification(**notification.dict())
    db.add(db_notif)
    db.commit()
    return {"status": "ok", "message": "Notification stored"}
