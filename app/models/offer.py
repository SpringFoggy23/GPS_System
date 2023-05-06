from sqlalchemy import Column, String, Integer, orm
from app.models.base import Base
import datetime


class Offer(Base):
     __abstract__ = True # 抽象类 不会生成表
     #id = Column(Integer, unique=True, autoincrement=True)
     date = Column(String(30), nullable=False)
     owner = Column(String(30), default='未名')
     gpa = Column(String(4))
  
     def __init__(self,date,owner,gpa):
        super(Offer,self).__init__()
        #self.id=id
        self.date=date
        self.owner=owner
        self.gpa=gpa

