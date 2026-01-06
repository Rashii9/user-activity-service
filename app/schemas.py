from pydantic import BaseModel

class ActivityCreate(BaseModel):
    user_id: str
    action: str
