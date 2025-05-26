from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import logging
from sqlalchemy.orm import Session
import models, database
from database import SessionLocal, engine
import schemas

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
logging.basicConfig(level=logging.INFO)

bearer_scheme = HTTPBearer()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    email = f"{token}@example.com"
    role = "admin" if token.endswith("admin") else "user"
    return {"email": email, "role": role}

@app.get("/me", response_model=schemas.UserResponse)
def get_user(user=Depends(verify_token), db: Session = Depends(get_db)):
    # Store user in DB if doesn't exist
    db_user = db.query(models.User).filter(models.User.email == user["email"]).first()
    if not db_user:
        db_user = models.User(email=user["email"], role=user["role"])
        db.add(db_user)
        db.commit()
    return user
