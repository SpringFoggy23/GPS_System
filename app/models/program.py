from sqlalchemy import Column, String, Integer, orm, Float
from app.models.base import Base


class Program(Base):
    Name = Column(String(8), primary_key=True)
    UniversityName = Column(String(50))
    GPALow = Column(Float(precision=2))
    GPAUpper = Column(Float(precision=2))

    def update(self, Name,GPALow, GPAUpper):
        if(GPALow <= 0 or GPAUpper <= 0 or GPALow > 4 or GPAUpper > 4):
            print(" The value of GPA out of range")
            return 1
        elif(GPALow >= GPAUpper):
            return 2
        else:
            self.Name=Name
            self.GPALow = GPALow
            self.GPAUpper = GPAUpper
           # db.session.commit()
            return 0
