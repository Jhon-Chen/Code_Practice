"""
使用重定向作为POST请求的响应，而不是使用常规响应。重定向是一种特殊的响应，响应内容是URL，而不是包含HTML代码的字符串。
浏览器收到这种响应时，会向重定向的URl发起GET请求，显示页面的内容。
现在，由于最后一个请求时GET请求，所以浏览器的刷新命令能像预期那样正常使用了。
这个技巧称为 Post/重定向/Get模式
"""

"""
但这种方法优惠带来另一个问题。程序处理POST请求时，使用 form.name.data 获取用户输入的名字。
可是一旦这个请求结束，数据也就丢失了。因为这个POST请求使用重定向处理，所以程序需要保存输入的名字，
这样重定向后的请求才能获得并使用这个名字，从而构建真正的响应。
程序可以把数据存储在用户会话中，在请求之间“记住”数据。用户会话是一种私有存储，存在于每个连接到服务器的客户端中。
它就是请求上下文的变量，名为 session，像标准的Python字典一样操作。默认情况下，用户会话保存在客户端cookie中，
使用设置的SECRET_KEY进行加密签名。如果篡改了cookie中的内容，签名就会失效，会话也会失效。
"""
from flask import Flask, render_template, session, redirect, url_for
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
    return render_template('demo3_把表单渲染成HTML.html', form=form, name=session.get('name'))


if __name__ == "__main__":
    app.run(debug=True)