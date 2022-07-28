from datetime import datetime
from .config import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    age: Column(Integer, nullable=False)
    ht: Column(Float, nullable=False)
    gender: Column(String, nullable=False)

# class BodyMonitor(Base):
#     __tablename__ = "body_monitor"

#     id: Column(Integer, primary_key=True)
#     user_id: Column(Integer, ForeignKey("user.id"))
#     created_at: Column(DateTime, default=datetime.now, nullable=False)
#     wt: Column(Float)
#     smm: Column(Float) # 골격근량
#     ffm: Column(Float) # 체지방량 
#     pbf: Column(Float) # 체지방률
#     max_bp: Column(Integer)
#     min_bp: Column(Integer)
#     pulse: Column(Integer)