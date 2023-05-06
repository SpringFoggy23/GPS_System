from flask import Blueprint,render_template, request
from app.models.base import db
from app.models.offer import Offer
import datetime
format = '%Y-%m-%d'
offerBP = Blueprint('offer',__name__)
dt = datetime.datetime.now()

@offerBP.route('', methods=['GET'])
def get_offer():
    with db.auto_commit():
        offer = Offer()
        offer.date = dt.strftime(format)
        offer.owner = 'Jack'
        offer.gpa = '3.0'
        # 数据库的insert操作
        db.session.add(offer)

    return 'hello offer'

@offerBP.route('change_offer', methods=['GET'])
def change_offer():
    with db.auto_commit():
        offer = Offer.query.get(1)
        offer.owner = 'Mark'

    return '111'+request.method