"""
Flask 提供了 url_for() 辅助函数，它可以使用程序使用程序URL映射汇总保存的信息生成URL。
url_for() 函数最简单的用法是视图函数名（或者app.add_url_route()定义路由时使用的端点名）作为参数，返回对应的URL。
注：生成连接程序内不同路由的链接时，使用相对地址就足够了。如果要生成在浏览器之外使用的链接，则必须使用绝对地址。

使用 url_for() 生成动态地址时，将动态部分作为关键字参数传入。
比如：url_for('user', name='jhon', _external=True)
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)