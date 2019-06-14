"""
Flask从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。请求对象就是一个很好的例子，它封装了客户端发送的HTTP请求。
要让视图函数能够访问请求对象，一个显而易见的方式就是将其作为参数传递到视图函数中，不过这会导致程序中的每个视图函数都增加了一个参数。除了访问请求对象，如果视图函数在处理请求时还访问其他对象，情况就会变得更糟糕。

为了避免大量参数使视图函数变得杂乱，Flask使用上下文临时把某些对象变为全局可访问。
"""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    # Flask 使用上下文让特定的变量（request）在一个线程中全局可以访问
    """Flask中有两种上下文：程序（应用）上下文和请求上下文
        程序上下文：current_app  当前激活程序的程序实例
                   g            处理请求时用作临时存储的对象。每次请求都会重设这个变量
        请求上下文：request      请求对象，封装了客户端发出的HTTP请求中的内容
                   session      用户会话，用于存储请求之间需要记住的值的字典"""
    user_agent = request.headers.get('User-Agent')
    return '<p>Your Browser is %s</p>' % user_agent


if __name__ == "__main__":
    app.run(debug=True)