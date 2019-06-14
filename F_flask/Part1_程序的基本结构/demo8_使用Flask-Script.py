from flask import Flask
"""
Flask-Script是一个Flask扩展，为Flask程序添加了一个命令行解释器。Flask-Script自带了一组常用选项，而且还支持自定义命令。
使用：pip install flask-script 安装
"""
from flask_script import Manager

app = Flask(__name__)
# 把程序的实例app作为参数传给构造函数，初始化类的实例
manager = Manager(app)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    # 注意，这里使用manager.run()来启动
    manager.run()