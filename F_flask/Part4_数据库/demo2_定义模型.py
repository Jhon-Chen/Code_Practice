"""
模型这个术语表示程序使用的持久化实体。在ORM中，模型一般是一个Python类，类中的属性对应数据库表中的列。
Flask-SQLAlchemy创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函数，可用于定义模型的结构。
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    """类变量__tablename__定义在数据库中使用的表名。如果没有定义，Flask-SQLAlchemy会使用一个
    默认的名字 """
    __tablename__ = 'roles'
    """db.Column类构造函数的第一个参数是数据库列和模型属性的类型"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    """Flask-SQLAlchemy要求每个模型都要定义主键"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    """虽然没有强制要求，但是这两个模型都定义了__repr()__方法，返回一个具有可读性的字符串表示模型
    可以在调试和测试时使用"""
    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)