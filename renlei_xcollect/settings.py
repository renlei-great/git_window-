import os


# 根目录路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 拼接resource路径
RESOURCE_PATH = os.path.join(BASE_DIR, 'resource')

# PostgreSQL --------测试环境
REMOTE_DATABASE = ''
REMOTE_USER = ''
REMOTE_PORT = ''
REMOTE_HOST = ''
REMOTE_PASSWORD = ''

