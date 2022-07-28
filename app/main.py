from fastapi import FastAPI, Query, Path, Depends
from .schema import UserSchema, BodyMonitorSchema
import json
from .model import User
from sqlalchemy.orm import Session
from .config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Create
@app.post("/body_monitor/{user_id}")
async def create_body_monitor(
    body_monitor:BodyMonitorSchema,
    user_id: int = Path(title="ID of User", ge=1)):
    return {"message": "success"}

# Read
@app.get("/body_monitor/{user_id}")
async def get_body_monitors_of_user(
    user_id: int = Path(title="ID of User", ge=1),
    page:int | None =1,
    limit:int|None=20):
    return {"message": "Hello World"}

# Read2
@app.get("/users")
async def get_user_list(db: Session = Depends(get_db)):
    print(db.query(User).first())
    print("HI!!!")


    users = Session().query(User).first()
    print("HI2!!!")
    return {"message": "Hello World"}


# Update
@app.put("/body_monitor/{body_monitor_id}")
async def update_body_monitor(
    body_monitor_id: int = Path(title="ID of body_monitor", ge=1)):
    return {"message": "success"}

# Delete
@app.post("/body_monitor/{body_monitor_id}")
async def delte_body_monitor(
    body_monitor_id: int = Path(title="ID of body_monitor", ge=1)):
    return {"message": "success"}