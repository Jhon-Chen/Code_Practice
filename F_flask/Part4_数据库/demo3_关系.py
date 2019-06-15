import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""关系型数据库使用关系把不同的表汇总的行联系起来。"""

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    """添加到Role模型中的users属性代表这个关系的面向对象视角。对于一个Role类的实例，其users属性将返回与角色相关联的用户组成的列表。
    db.relationship()的第一个参数表明这个关系的另一端是哪个模型。如果模型尚未定义，可使用字符串形式指定。后面的backref参数向模型
    中添加一个role属性，从而定义反向关系。这一属性可替代role_id访问Role模型，此时获取的是模型对象，而不是外键的值。"""
    users = db.relationship('User', backref='role')
    """
    常用的SQLAlchemy关系选项：
    backref                     在关系的另一个模型里添加反向引用
    primaryjoin                 明确指定两个模型之间使用的联络条件
    lazy                        指定如何加载相关记录。可选值有select（首次访问时按需加载）、immediate（源对象加载后就加载）、
                                joined（加载记录，但使用联结）、subquery（立即加载，但是用子查询）、noload（永不加载）、
                                dynamic（不加载记录，但提供加载记录的查询）
    uselist                     如果设定为False，不使用列表，而使用标量值
    order_by                    指定关系中记录的排序方式
    secondary                   指定多对多关系中关系表的名字
    secondaryjoin               SQLAlchemy无法自行决定时，指定多对多关系中的二级联结条件
    """
    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    """关系使用users表中的外键连接了两行，添加到User模型中的role_id列被定义为外键，就是这个外键建立起了关系。
    传给db.ForeignKey()的参数'roles.id'表明，这列的值是roles表中行的id值"""
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    """一对一关系可以用前面的一对多表示，但调用db.relationship()时要把uselist设为False。多对一也可以用一对多表示，对调两个表即
    可，或者把外键和db.relationship()都放在多的一侧。多对多后面再涉及。"""
    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)