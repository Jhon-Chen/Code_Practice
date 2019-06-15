"""
Flask-SQLAlchemy是一个Flask扩展，简化了在Flask程序中使用SQLAlchemy的操作。
SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后台。
程序使用的数据库URL必须保存到Flask配置对象的SQLALCHEMY_DATABASES_URI键中。配置对象中还有一个很有用的选项，
即SQLALCHEMY_COMMIT_ON_TEARDOWN键，将其设置为True时，每次请求结束后都会自动提交数据库中的变动。
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# db对象是SQLAlchemy类的实例，表示程序使用了数据库，同时还获得了Flask-SQLAlchemy提供的所有功能
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)