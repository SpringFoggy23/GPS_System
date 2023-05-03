from flask import Blueprint,render_template, request
from app.models.base import db
from app.models.TaughtCourseOffer import TaughtCourseOffer

TaughtCourseOfferBP = Blueprint('TaughtCourseOffer',__name__)

@TaughtCourseOfferBP.route('', methods=['GET'])
def get_TaughtCourseOffer():
        with db.auto_commit():
            taught_course_offer=TaughtCourseOffer()
            #taughtcourseoffer=taughtcourseoffer("Toronto University","Medicine")
            taught_course_offer.universityname="Havard university"
            taught_course_offer.programName="Medicine"
            db.session.add(taught_course_offer)
        return "hello TaughtCourseOffer"