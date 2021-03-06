"""
请求完成后， 有时需要让用户知道状态发生了变化。这里可以使用确认消息、警告或者错误提醒。
"""
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'code'


class NameForm(Form):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['POST', 'GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    else:
        # 在这里添加flash消息，并且需要在模板中渲染flash消息
        """
        在模板中使用循环是因为在之前的请求循环中每次调用flash()函数时都会生成一个消息，所以有可能有多个消息在排队等待显示。
        get_flashed_messages() 函数获取的消息在下次调用时不会再次返回，因此Flash消息只显示一次，然后就消失了。
        """
        flash("Please type your name here")
    if form.name.data != "jhon":
        flash('Welcome Stranger!')
    else:
        flash('Oh~ I love Gakki too~')
    return render_template('demo3_把表单渲染成HTML.html', form=form, name=session.get('name'))


if __name__ == "__main__":
    app.run(debug=True)