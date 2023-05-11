from sqlalchemy import Column, String, Integer, orm, Float
from app.models.base import Student


class Alumni(Student):
    AnonymousName = Column(String(8), primary_key=True)
    Status = Column(String(50))


    def update(self, Status):
        self.Status = Status

