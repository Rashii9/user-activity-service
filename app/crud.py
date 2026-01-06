from sqlalchemy.orm import Session
from .models import UserActivity

def create_activity(db: Session, user_id: str, action: str):
    activity = UserActivity(user_id=user_id, action=action)
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

def get_activities(db: Session):
    return db.query(UserActivity).all()
