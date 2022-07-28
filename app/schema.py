from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    id: int
    age: int
    ht: float
    gender: str

    class Config:
        orm_mode = True

class BodyMonitorSchema(BaseModel):
    created_at: datetime
    wt: float | None = None
    smm: float | None = None
    ffm: float | None = None
    pbf: float | None = None
    max_bp: int | None = None
    min_bp: int | None = None
    pulse: int | None = None
    class Config:
        orm_mode = True
    
class BodyMonitorUpdateSchema(BaseModel):
    wt: float | None = None
    smm: float | None = None
    ffm: float | None = None
    pbf: float | None = None
    max_bp: int | None = None
    min_bp: int | None = None
    pulse: int | None = None
    class Config:
        orm_mode = True