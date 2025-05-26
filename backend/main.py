from fastapi import FastAPI, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, schemas, database
import requests
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from database import Base, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)




origins = ["*"]  # Allow all origins for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bearer_scheme = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    token = credentials.credentials
    email = f"{token}@example.com"
    role = "admin" if token.endswith("admin") else "user"
    return {"email": email, "role": role}



# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_task", response_model=schemas.Task)
def create_task(
	task: schemas.TaskCreate, 
	db: Session = Depends(get_db), 
	user=Depends(verify_token)
	):
	
    db_task = models.Task(title=task.title, description=task.description, user_email=user["email"], user_role=user["role"])
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    
    #Notify user 
    requests.post("http://notification_service:8001/notify", json={"task_title": db_task.title, "user_email": user["email"]})
    
    #Simulate donation 
    requests.post("http://donation_service:8002/donate", json={"user_email": user["email"], "amount": 1.0})
    
    return db_task

@app.get("/list_tasks", response_model=list[schemas.Task])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()
