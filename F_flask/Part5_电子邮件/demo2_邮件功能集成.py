import os
from flask import Flask, render_template, flash, session, redirect, url_for
from flask_mail import Mail
from flask_mail import Message
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 初始化Flask-Mail
app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASK_MAIL_SENDER'] = 'Flasky Admin cyf15751002326@gmai.com'
app.config['FLASK_ADMIN'] = os.environ.get('FLASK_ADMIN')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jhonchen:2553522375@47.100.200.127:3306/flask_practice'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'code'
"""电子邮件的收件人保存在环境变量FLASK_ADMIN中，在程序启动过程中，它会加载到一个同名配置变量中。我们要创建两个模板文件，分别用于
渲染纯文本和HTML版本的邮件正文。这两个模板文件都保存在templates文件夹下的mail子文件夹，以便和普通模板区分开。电子邮件的模板中要
有一个模板参数是用户，因此调用send_mail()函数时都要以关键字参数的形式传入用户。"""
db = SQLAlchemy(app)
manager = Manager(app)

migrate = Migrate(app, db)
"""manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令"""
manager.add_command('db', MigrateCommand)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASK_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


"""这个函数用到了两个程序特定配置项，分别定义邮件主题的前缀和发件人的地址。send_email函数的参数分别为收件人地址、主题、
渲染邮件正文的模板和关键字参数列表。指定模板时不能包含扩展名，这样才能使用两个模板分别渲染纯文本正文和富文本正文。调用者将
关键字参数传给render_template()函数，以便在模板中使用，进而生成电子邮件正文。
index()视图函数很容易被扩展，这样每当表单接收新名字时，程序都会给管理员发送一封电子邮件。"""


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


@app.route('/')
def index():
    form = NameForm()
    user = User.query.filter_by(username=form.name.data).first()
    if user is None:
        user = User(username=form.name.data)
        db.session.add(user)
        session['known'] = False
        if app.config['FLASK_ADMIN']:
            send_email(app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('demo2.html', form=form, name=session.get('name'), known=session.get('known', False))


if __name__ == '__main__':

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
