from sqlalchemy import Column, String, Integer, orm, Float
from app.models.base import Student


class UICer(Student):
    Name = Column(String(8), primary_key=True)
    Email = Column(String(24), unique=True, nullable=True)
    password = Column('password', String(100))
    GPA = Column(Float(.2))

   
