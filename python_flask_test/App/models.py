from App.ext import db
# from flask_sqlalchemy import SQLAlchemy
#
#
# db = SQLAlchemy()
#
# def init_models(app):
#     db.init_app(app=app)

class usertable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))