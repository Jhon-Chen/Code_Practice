"""程序实例使用run方法启动Flask集成的开发Web服务器"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello world</h1>'


if __name__ == '__main__':
    app.run(debug=True)
