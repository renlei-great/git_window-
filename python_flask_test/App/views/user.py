from flask import Blueprint
from App.models import db
from App.models import usertable

user = Blueprint('user', __name__)


@user.route('/user/')
def useradd():
    return '注册用户'

@user.route('/createdb/')
def createdb():
    db.create_all()
    return '建表成功'

@user.route('/adduser/')
def adduser():
    u = usertable()
    u.username = 'renlei'
    db.session.add(u)
    db.session.commit()
    return '创建成功ok'

@user.route('/dorp/')
def dorptable():
    db.drop_all()
    return '删除成功'