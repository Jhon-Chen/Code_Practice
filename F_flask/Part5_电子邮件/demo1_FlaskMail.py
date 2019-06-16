import os
from flask import Flask
from flask_mail import Mail
"""Flask-Mail连接到简单邮件传输协议（Simple Mail Transfer Protocol, SMTP）服务器，并把邮件交给这个服务器发送。如果不进行配置，
Flask-Mail会连接localhost上的端口25，无需验证即可发送电子邮件。"""
"""Flask-Mail SMTP服务器的配置
    MAIL_SERVER         localhost           电子邮件服务器的主机名或IP地址
    MAIL_PORT           25                  电子邮件服务器的端口
    MAIL_USE_TSL        False               启动传输层安全（Transport Layer Security, TLS）协议
    MAIL_USE_SSL        False               启用安全套接层（Secure Sockets Layer, SSL）协议
    MAIL_USERNAME       None                邮件账户的用户名
    MAIL_PASSWORD       None                邮件账户的密码
在开发过程中，如果连接到外部SMTP服务器，则可能更方便。"""

# 初始化Flask-Mail
app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
"""千万不要把账户密令直接写入脚本，特别是当时你计划开源自己的作品时。为了保护账户信息，你需要让脚本从环境中导入敏感信息"""


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
