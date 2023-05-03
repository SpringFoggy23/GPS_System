from sqlalchemy import Column, String, Integer, orm, Float
from app.models.base import Base


class TaughtCourseOffer(Base):
    #universityname = Column(String(50), primary_key=True, autoincrement=True)
    universityname = Column(String(50))
    programName=Column(String(30), primary_key=True)

    # def __init__(self, universityname, programName):
    #     self.universityname = universityname
    #     self.programName = programName
    
    def SubmitTaughtOffer(self, Title, CompanyName, date, GPA):
        # 将提供的参数值存储在类属性中
        self.Title = Title
        self.CompanyName = CompanyName
        self.date = date
        self.GPA = GPA
        
        # 在此处可以添加其他实现逻辑，例如将此条记录添加到数据库中等
        # 请注意，为了简单起见，下面的代码只是在控制台上打印一条消息
        print(f"Offer for {self.programName} has been submitted to {self.CompanyName} on {self.date}.")
        
    def SearchTaughtOffer(self, ProgramName):
        # 在此处可以添加实现逻辑，例如从数据库中检索记录等
        # 请注意，为了简单起见，下面的代码只是在控制台上打印一条消息
        print(f"Searching for job offers for {ProgramName}...")