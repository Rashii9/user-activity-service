from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from prometheus_client import generate_latest
from fastapi.responses import Response

from .database import SessionLocal, engine
from . import models, schemas, crud
from .metrics import REQUEST_COUNT

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Activity Service")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/activity")
def log_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    REQUEST_COUNT.inc()
    return crud.create_activity(db, activity.user_id, activity.action)

@app.get("/activities")
def read_activities(db: Session = Depends(get_db)):
    return crud.get_activities(db)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
