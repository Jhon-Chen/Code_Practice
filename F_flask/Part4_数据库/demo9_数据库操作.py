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
    manager.run()

"""检查并修正迁移脚本之后，我们可以使用 db upgrade 命令把迁移应用到数据库中:
(venv) E:\GitHub\Code_Practice\F_flask\Part4_数据库>python demo8_数据库迁移.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.

(venv) E:\GitHub\Code_Practice\F_flask\Part4_数据库>
    对于第一个迁移来说，其作用和调用db.create_all()方法一样。但在后续的迁移中，upgrade命令能把改动应用到数据库中，且不
    影响其中保存的数据。"""