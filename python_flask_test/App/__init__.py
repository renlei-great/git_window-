from flask import Flask

from .ext import init_ext
from .views import register_blueprints

def create_app():
    app = Flask(__name__)

    # 配置文件
    # uri 数据库+驱动://用户名:密码@主机:端口/具体那一个库
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ubuntu@localhost/flask_test"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 注册蓝图
    register_blueprints(app)
    # 第三方扩展库
    init_ext(app)





    return app