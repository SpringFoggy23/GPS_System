from turtle import update
from sqlalchemy import Column, String
from app.models.base import Base


class Program(Base):
    CourseNameList = Column(String(50), primary_key=True)
    UniversityName = Column(String(50))
    ProgramName = Column(String(10))

    # def __init__(self, Name, UniversityName, GPALow, GPAUpper):
    #     super(Program, self).__init__(Name, UniversityName, GPALow, GPAUpper)

    def addNewcourse(self, new):
        self.CourseNameList = update(new)

