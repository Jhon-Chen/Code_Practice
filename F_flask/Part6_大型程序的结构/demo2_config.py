"""程序经常需要设定多个配置。这方面最好的例子就是开发、测试和生产环境要使用不用的数据库，这样才不会彼此影响。
我们不再使用之前例子中简单的字典状结构配置，而使用层次结构的配置类。config.py文件的内容如下："""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'Flasky Admin 2553522375@qq.com'
    FLASK_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                             'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

"""基类Config中包含通用配置，子类分别定义专用的配置。如果需要，你还可添加其他配置类。
为了让配置方式更加灵活且安全，某些配置可以从环境变量中导入。
在三个子类中，SQLALCHEMY_DATABASE_URI变量都被指定了不同的值。这样程序就可在不同的配置环境中运行，每个环境都使用不同的数据库。
配置类可以定义init_app()类方法，其参数是程序实例。在这个方法中，可以执行对当前环境的配置初始化。现在，基类Config中的init_app()
方法为空。
在这个配置脚本末尾，config字典中注册了不同的配置环境，而且还注册了一个默认配置。"""