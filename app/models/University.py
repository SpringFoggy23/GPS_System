from sqlalchemy import Column, String, list
from app.models.program import Program

class University(Program):
    Name = Column(String(50))
    ProgramList = CourseNameList = Column(list(50), primary_key=True)

    def addProgram(self, newpro):
        self.addProgram = list.append(newpro)