from flask import Blueprint,render_template, request
from app.models.base import db
from app.models.ResearchOffer import ResearchOffer

ResearchOfferBP = Blueprint('ResearchOffer',__name__)

@ResearchOfferBP.route('', methods=['GET'])

def send_ResearchOffer():
        with db.auto_commit():
            #program = Program(Name = 'ComputerScience',UniversityName = 'UIC',GPALow = float(3.0),GPAUpper = float(3.8))
            research_offer=ResearchOffer()
            research_offer.Supervisor="Dr.Hao"
            research_offer.Name="Finance And Options"
            research_offer.ResearchTopic="Future"
            research_offer.No_Topic=15
            research_offer.No_research=7
             
            db.session.add(research_offer)
        return 'hello Successfully'

@ResearchOfferBP.route('Submit', methods=['GET'])

def SubmitResearchOffer():
        with db.auto_commit():
            research_offer=ResearchOffer()
            research_offer.Supervisor="Dr.Wang"
            research_offer.Name="OfferFromUCL"
            research_offer.ResearchTopic="EarthScience"
            research_offer.No_Topic=9
            research_offer.No_research=13
             
            db.session.add(research_offer)
        return 'Submit Successful'

@ResearchOfferBP.route('search', methods=['GET'])
def search():
    with db.auto_commit():
        #仅可支持主键查询
        researchOffer = ResearchOffer.query.get('OfferFromUCL')
        answer= researchOffer.Supervisor +"      "+researchOffer.ResearchTopic+"     "+ str(researchOffer.No_Topic) +"   " 
    return answer