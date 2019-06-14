from flask import Flask, make_response, redirect, abort

app = Flask(__name__)
"""请求钩子帮助我们在处理请求之前或者之后执行一段代码
    请求钩子使用修饰器实现。Flask支持一下四种钩子：
    1.before_first_request: 注册一个函数，在处理第一个请求之前运行
    2.before_request: 注册一个函数，在每次请求之前运行
    3.after_request: 注册一个函数，如果没有未处理的异常，在每次请求之后运行
    4.teardown_request: 注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行
在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量g"""


@app.route('/')
def index():
    """
    Flask调用视图函数之后，会将其返回值作为响应的内容。HTTP响应中一个很重要的部分是状态码，Flask默认设为200，这个代码表示请求已经被成功处理了。
    如果视图函数返回的响应需要使用不同的状态码，那么可以把数字代码作为第二个返回值，添加到响应文本之后。
    """
    return 'Hello World!', 520


@app.route('/demo')
def demo():
    """
    Flask视图还可以返回Response对象。make_response()函数可以接受1~3个参数，并返回一个Response对象。
    有时我们需要在视图函数中进行这种转换，然后在响应对象上调用各种方法，进一步设置响应。
    比如此处创建了一个响应对象，然后设置了cookie。
    """
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/demo1')
def demo1():
    """
    有一种名为重定向的特殊响应类型。这种响应没有页面文档，只告诉浏览器一个新地址用以加载新页面。
    重定向经常用302状态码表示。
    """
    return redirect('http://47.100.200.127')


@app.route('/demo2/<user_id>')
def demo2(user_id):
    """还有一种特殊的响应有abort函数生成，用于处理错误。"""
    user = int(user_id)
    if not user:
        abort(404)
    return '%s' % user


if __name__ == "__main__":
    app.run(debug=True)