from sqlalchemy import Column, String, Integer, orm
from app.models.base import Base
import datetime


class Offer(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(30), nullable=False)
    owner = Column(String(30), default='未名')
    gpa = Column(String(4))
    