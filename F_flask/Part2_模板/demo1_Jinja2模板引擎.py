"""
视图函数的作用很明确，即生成请求的响应。对最简单的请求来说，这就足够了。
但是一般而言，请求会改变程序的状态，而这种变化也会在视图函数中产生。
例如，用户在网站注册一个新的账户。用户在表单中输入电子邮件地址和密码，然后点击提交按钮。服务器接收到包含用户输入数据的请求，
然后Flask把请求分发到处理注册请求的视图函数。这个视图函数需要访问数据库，添加新用户，然后生成响应回送浏览器。
这两个过程分别称为 业务逻辑 和 表现逻辑。把两种逻辑混在一起回导致代码的难易理解和维护。把表现逻辑移到模板中能够提升程序的可维护性。

模板是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。使用真实值替换变量，
再返回最终得到的响应字符串，这一过程称为渲染。Flask为了渲染模板，使用了Jinja2这个模板引擎。
默认情况下，Flask在程序文件夹中的templates文件夹中寻找模板。
"""
from flask import Flask, render_template
# Flask提供的render_template函数把Jinja2模板引擎集成到了程序中
app = Flask(__name__)


@app.route('/')
def index():
    # render_template函数的第一个参数是模板的文件名。随后的参数都是键值对，表示模板中变量对应的真实值
    return render_template('demo1.html')


@app.route('/demo/<name>')
def demo(name):
    # 此处模板收到一个名为name的变量。 其中name=name是关键字参数，左边的name表示的是模板中的占位符；右边的name表示的是当前
    # 作用域中的变量，表示同名参数的值
    return render_template('demo1_Jinja2.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)