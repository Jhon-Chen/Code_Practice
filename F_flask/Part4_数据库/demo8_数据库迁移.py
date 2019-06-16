"""更新表的更好方法是使用数据库迁移框架。源码版本控制工具可以跟踪源码文件的变化，类似地，数据库迁移框架能跟踪数据库模式的变化，
然后增量式变化应用到数据库中"""
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from flask_script import Shell, Manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jhonchen:2553522375@47.100.200.127:3306/flask_practice'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
manager = Manager(app)

migrate = Migrate(app, db)
"""manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令"""
manager.add_command('db', MigrateCommand)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    # 更新现有数据库表的粗暴方式是先删除旧表再重新创建
    db.drop_all()
    db.create_all()
    # 下面这段代码创建了一些用户。
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_jhon = User(username='jhon', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)

    db.session.add_all([admin_role, mod_role, user_role, user_david, user_jhon, user_susan])

    db.session.commit()

    """在终端中使用命令 python demo8_数据库迁移.py db init 就可以使用init子命令创建迁移仓库，这个命令会创建
    migrations文件夹，所有迁移脚本都存放其中。
    数据库迁移仓库中的文件要和程序的其他文件一起纳入版本控制"""

    manager.run()
    """在Alembic中，数据库迁移用迁移脚本表示。脚本中有两个函数，分别是upgrade()和downgrade()。
    upgrade()函数把迁移中的改动应用到数据库中，downgrade()函数则将改动删除。Alembic具有添加和删除改动的能力，
    因此数据库可重设到修改历史的任意一点。
    我们可以使用revision命令收到创建Alembic迁移，也可使用migrate命令自动创建。手动创建的迁移只是一个骨架，upgrade()
    和downgrade()函数都是空的，开发者要使用Alembic提供的Operations对象指令实现具体操作。自动创建的迁移会根据模型定义
    和数据库当前状态之间的差异生成upgrade()和downgrade()函数的内容。
    在终端中使用migrate子命令自动创建迁移脚本"""