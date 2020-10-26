from .first_blue import first
from .user import user

# 蓝图配置列表
blueprint__config = [first, user]


def register_blueprints(app):
    '''注册蓝图对象'''
    # 循环注册每一个配置列表中的对象
    for name in blueprint__config:
        app.register_blueprint(name)