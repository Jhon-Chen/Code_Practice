from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jhonchen:2553522375@47.100.200.127:3306/flask_practice'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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
    """模型的构造函数接受的额参数是使用关键字指定的模型属性初始值。注意，role属性也可用，虽然他不是真正的数据库列
    但确实一对多关系的高级表示。这些新建对象的id属性并没有明确设定，因为主键是由Flask-SQLAlchemy管理的。
    现在这些对象只存在于Python中，还未写入数据库。
    通过数据库会话管理对数据库所做的改动，在Flask-SQLAlchemy中，会话由db.session表示。准备把对象写入数据库之前，
    先要将其添加到会话中。"""
    db.session.add_all([admin_role, mod_role, user_role, user_david, user_jhon, user_susan])
    """为了把对象写入数据库，我们要调用commit()方法提交会话"""
    db.session.commit()

    """数据库会话能保证数据库的一致性。提交操作使用原子方式把会话中的对象全部写入数据库。如果在写入会话的过程中发生了
    错误，整个会话都会失效。如果你始终把改动放在会话中提交，就能避免因部分更新导致的数据库不一致。
    数据库会话也可以回滚。调用db.session.rollback()后，添加到数据库会话中的所有对象都会还原到他们在数据库时的状态。"""
    app.run(debug=True)