from flask import Flask
from flask_sqlalchemy import SQLAlchemy #数据库管理
#package标识

app = Flask(__name__) #初始化，被调用 __name__ 为模块名app
print(__name__)
print('==============================')
app.config.from_object('config')#导入配置文件
db = SQLAlchemy(app)#创建 SQLAlchemy 对象时候把 Flask 应用传递给它作为参数。


import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models