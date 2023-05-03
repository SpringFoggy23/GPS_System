from sqlalchemy import Column, String, Integer, orm, Float
from app.models.base import Base

class ResearchOffer(Base):
    Supervisor = Column(String(50))
    Name=Column(String(30), primary_key=True)
    ResearchTopic=Column(String(50))
    No_Topic=Column(Integer)
    No_research=Column(Integer)

    # def __init__(self, supervisor, name, research_topic, no_papers, no_research):
    #     self.supervisor = supervisor
    #     self.name = name
    #     self.research_topic = research_topic
    #     self.no_papers = no_papers
    #     self.no_research = no_research
    
    def SubmitResearchOffer(self, supervisor, name, date, no_papers, no_research):
        # 研究项目提交功能的实现代码,将提供的参数值存储在类属性中
        self.supervisor = supervisor
        self.name = name
        self.date = date
        self.no_papers = no_papers
        self.no_research=no_research
        
    #     # 在此处可以添加其他实现逻辑，例如将此条记录添加到数据库中等
    #     print(f"Offer for {self.programName} has been submitted to {self.CompanyName} on {self.date}.")
    
    def SearchResearchOffer(self, program_name):
        # 研究项目搜索功能的实现代码
        print(f"Searching for job offers for {program_name}...")
        