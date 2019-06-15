"""
默认情况下，Flask-WTF能保护所有表单免受跨站请求伪造（Cross-Site Request Forgery, CSRF）的攻击。
为了实现CSRF保护，Flask-WTF需要程序设置一个密钥。Flask-WTF使用这个密钥生成加密令牌，再用令牌验证请求中
表单数据的真伪。
"""
from flask import Flask

app = Flask(__name__)
# 设置密钥
app.config['secret_key'] = 'hard to guess string'
# app.config 字典可用来存储框架、扩展 和程序本身的配置变量。使用标准字典语法就可以把配置添加进去
# 同时，这个对象还提供了一些方法，可以从文件或环境中导入配置值


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
