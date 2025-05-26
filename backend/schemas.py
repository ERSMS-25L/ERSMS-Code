from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_email: str
    user_role: str

    class Config:
        orm_mode = True
