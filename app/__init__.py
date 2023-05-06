from flask import Flask
from app.controller import TaughtCourseOffer, program,ResearchOffer,Student,Teacher,user,offer

# 定义注册蓝图方法
def register_blueprints(app):    
    app.register_blueprint(Student.studentBP,url_prefix='/Student')
    app.register_blueprint(Teacher.teacherBP,url_prefix='/Teacher')
    app.register_blueprint(ResearchOffer.ResearchOfferBP,url_prefix='/ResearchOffer')
    app.register_blueprint(TaughtCourseOffer.TaughtCourseOfferBP,url_prefix='/TaughtCourseOffer')
    app.register_blueprint(program.programBP, url_prefix='/program')
    app.register_blueprint(user.userBP,url_prefix='/user')
    app.register_blueprint(offer.offerBP,url_prefix='/offer')



# 注册插件(数据库关联)
def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    # create_all要放到app上下文环境中使用
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    # app.config.from_object('app.config.setting') # 基本配置(setting.py) 
    app.config.from_object('app.config.secure') # 重要参数配置(secure.py)
    # 注册蓝图与app对象相关联
    register_blueprints(app)
    # 注册插件(数据库)与app对象相关联
    register_plugin(app)
    # 一定要记得返回app
    return app