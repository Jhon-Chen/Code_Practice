"""
程序在收到客户端发来的请求时，要找到处理该请求的视图函数。为了完成这个任务，Flask会在程序的URL映射中查找请求的URL。
URL映射是URL和视图函数之间的对应关系。
Flask使用app.route修饰器或者非修饰器形式的 app.add_url_rule() 生成映射。
在虚拟环境的终端中： from demo6_请求调度 import app\r\n app.url_map\r\n 就可以查看到映射的关系
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)