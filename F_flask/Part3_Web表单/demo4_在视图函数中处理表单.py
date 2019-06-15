from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
app = Flask(__name__)
app.config['SECRET_KEY'] = 'do you know'


# 表单类的定义
class NameForm(Form):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField('Submit')


"""
app.route 修饰器添加的 methods 参数告诉Flask在URL映射中把这个视图函数注册为GET和POST请求的处理程序。
如果没指定methods参数，就只把视图函数注册为GET请求的处理程序。
简单的说，提交表单大都作为POST请求进行处理。 
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    # 局部变量 name 用来存放表单中输入的有效名字，如果没有输入，其值为None
    name = None
    # 在视图函数中创建一个NameForm类实例用于表示表单。
    form = NameForm()
    # 这里在提交表单后，如果所有数据都能被验证函数所接受，则处理表单数据，否则重新渲染表单
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('demo3_把表单渲染成HTML.html', form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)