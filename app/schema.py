from datetime import datetime

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: int
    age: int
    ht: float
    gender: str

    class Config:
        orm_mode = True

class BodyMonitorUpdateSchema(BaseModel):
    wt: float | None = Field(default=None, example=62.1)
    smm: float | None = Field(default=None, example=23.7)
    ffm: float | None = Field(default=None, example=22.1)
    pbf: float | None = Field(default=None, example=20.8)
    max_bp: int | None = Field(default=None, example=123)
    min_bp: int | None = Field(default=None, example=78)
    pulse: int | None = Field(default=None, example=82)
    class Config:
        orm_mode = True

class BodyMonitorSchema(BodyMonitorUpdateSchema):
    created_at: datetime
    class Config:
        orm_mode = True