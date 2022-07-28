from datetime import datetime, timedelta
from fastapi import FastAPI, Path, Depends
from .schema import UserSchema, BodyMonitorSchema,BodyMonitorUpdateSchema
from typing import List
from .model import BodyMonitor, User
from sqlalchemy.orm import Session
from .config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def _commit(db,data):
    db.add(data)
    db.commit()
    db.refresh(data)

app = FastAPI()

def time_setter(obj:datetime):
    if obj.microsecond >= 500_000:
        obj += timedelta(seconds=1)
    return obj.replace(microsecond=0)

# Create
@app.post("/body_monitor/user/{user_id}")
async def create_body_monitor(
    body_monitor:BodyMonitorSchema,
    db: Session = Depends(get_db),
    user_id: int = Path(title="ID of User", ge=1)
    ):
    body_monitor_query = db.query(BodyMonitor).filter_by(
        user_id = user_id,
        created_at = time_setter(body_monitor.created_at)
    ).first()
    if body_monitor_query is not None:
        return {"success":True, "data":"data already exists"}
    body_monitor = BodyMonitor(
        user_id = user_id, **body_monitor.dict()
    )
    
    _commit(db,body_monitor)

    return {"success":True, "data" :body_monitor}

# Read
@app.get("/body_monitor/user/{user_id}", response_model=List[BodyMonitorSchema])
async def get_body_monitors_of_user(
    user_id: int = Path(title="ID of User", ge=1),
    db: Session = Depends(get_db),
    page:int | None =1,
    limit:int|None=20):

    body_monitors = db.query(BodyMonitor
        ).filter_by(user_id=user_id
        ).offset((page-1)*limit
        ).limit(limit
        ).all()

    return body_monitors

# Read2
@app.get("/users", response_model=List[UserSchema])
async def get_user_list(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return users


# Update
@app.put("/body_monitor/{body_monitor_id}")
async def update_body_monitor(
    body_monitor_update:BodyMonitorUpdateSchema,
    db: Session = Depends(get_db),
    body_monitor_id: int = Path(title="ID of body_monitor",
    ge=1)):

    body_monitor_query = db.query(BodyMonitor).filter_by(id=body_monitor_id).first()
    if body_monitor_query is None:
        return {"success":False, "data":"data not exists"}
    body_monitor_dict = {
        key:value for key,value 
        in body_monitor_update.dict().items()
        if (value and value != 0)
    }
    db.query(BodyMonitor
        ).filter_by(id=body_monitor_id
        ).update(body_monitor_dict)
    
    _commit(db,body_monitor_query)

    return {"success":True, "data":body_monitor_query}


# Delete
@app.post("/body_monitor/{body_monitor_id}")
async def delete_body_monitor(
    db: Session = Depends(get_db),
    body_monitor_id: int = Path(title="ID of body_monitor",
    ge=1)):

    body_monitor_query = db.query(BodyMonitor).filter_by(id=body_monitor_id).first()
    if (
        body_monitor_query is None  or
        body_monitor_query.deleted_at is not None):
        return {"success":False, "data":"data not exists"}
    
    db.query(BodyMonitor
        ).filter_by(id=body_monitor_id
        ).update({"deleted_at":datetime.now()})
    
    _commit(db, body_monitor_query)
    return {"success":True, "data":""}