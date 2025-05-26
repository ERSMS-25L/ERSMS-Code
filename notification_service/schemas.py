from pydantic import BaseModel

class  NotificationCreate(BaseModel):
    user_email: str
    task_title: str
