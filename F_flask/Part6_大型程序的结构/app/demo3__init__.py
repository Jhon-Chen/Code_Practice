# app/__init__.py：程序包的构造文件
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

"""程序包用来保存程序的所有代码、模板和静态文件。我们可以把这个包直接成为app（应用），如果有需求，也可以使用一个程序专用名字。
templates和static文件夹是程序包的一部分，因此这两个文件夹被移到了app中。数据库模型和电子邮件支持函数也被移到了这个包中，分别保存
为app/models.py和app/email.py。"""

"""使用程序工厂函数：
在单个文件中开发程序很方便，但却有个很大的缺点，因此程序在全局作用域中创建，所有无法动态修改配置。运行脚本时，程序实例已经创建，
再修改配置为时已晚。这一点对单元测试尤其重要，因为有时为了提高测试覆盖度，必须在不同的配置环境中运行程序。
这个问题的解决方法是延迟创建程序实例，把创建过程移到可显式调用的工厂函数中。这种方法不仅可以给脚本流出配置程序的时间，还能够创建
多个程序实例，这些实例有时在测试中非常有用。程序的工厂函数在app包的构造文件中定义。"""

"""构造文件导入了大多数正在使用的Flask扩展。由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入函数。
create_app()函数就是程序的工厂函数，接受一个函数，是程序使用的配置名。配置类在config.py文件中定义，其中保存的配置可以使用
Flask app.config配置对象提供的from_object()方法直接导入程序。至于配置对象，则可以通过名字从config字典中选择。程序创建并配置好
后，则可以通过名字从config字典中选择。程序创建并配置好后，就能初始化扩展了。在之前创建的扩展对象上调用init_app()可以完成初始化过
程。"""

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db.SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 附加路由和自定义的错误页面
    return app


"""工厂函数返回创建的程序示例，不过要注意，现在工厂函数创建的程序还不完整，因为没有路由和自定义的错误页面处理程序。"""
