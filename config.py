import os

BASE_DIR= os.getcwd()

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # 模板文件的路径

STATICFILES_DIR = os.path.join(BASE_DIR, 'static')  # 静态文件的路径

SQLALCHEMY_DATABASE_URI = "mysql://device:ZC2019@bi.cbpm@192.168.31.63:3306/train"  # 数据库URI

SQLALCHEMY_TRACK_MODIFICATIONS = False  # 查询跟踪
