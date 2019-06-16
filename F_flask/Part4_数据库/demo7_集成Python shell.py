"""每次启动shell会话都要导入数据库实例和模型，这真是份枯燥的工作。为了避免一直重复导入，我们恶意做些配置，让Flask-Script的
shell命令自动导入特定对象。
若想把对象添加到导入列表中，我们要为shell命令注册一个make_context回调函数。"""

from flask import Flask, flash, session, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Shell

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jhonchen:2553522375@47.100.200.127:3306/flask_practice'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'code'
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


class NameForm(Form):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField('Submit')


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", shell(make_context=make_shell_context))


@app.route('/', methods=['POST', 'GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('demo6.html', form=form, name=session.get('name'), known=session.get('known', False))


if __name__ == "__main__":
    app.run(debug=True)
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

    admin_role.name = 'Administrator'
    db.session.add(admin_role)
    db.session.commit()

    db.session.delete(mod_role)
    db.session.commit()

    Role.query.all()
    User.query.all()

    User.query.filter_by(role=user_role).all()

    str(User.query.filter_by(role=user_role))
