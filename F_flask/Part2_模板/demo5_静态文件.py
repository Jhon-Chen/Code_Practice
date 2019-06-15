"""Flask 中默认的static静态文件包，可以直接通过 地址/文件名 来访问"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)