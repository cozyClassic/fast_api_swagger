from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    user_id: int
    age: int
    ht: float
    gender: str

class BodyMonitorSchema(BaseModel):
    monitor_id: int
    user_id: int
    created_at: datetime
    weight: float
    skeletal_muscle_mass: float
    fat_weight: float
    fat_percentage: float
    blood_pressure_highest: int
    blood_pressure_lowest: int
    pulse: int