"""manage.py 脚本启动程序"""

# !/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", shell(make_shell_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests.
    manager.command 修饰器让自定义命令变得简单。修饰函数名就是命令名，函数的文档字符串会显示在帮助消息中。test()函数的定义体中
    调用了unittest包提供的测试运行函数。
    单元测试可使用下面的命令运行：
    python manage.py test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

"""这个脚本先创建程序。如果已经定义了环境变量FLASK_CONFIG,则从中读取配置名；否则使用默认配置。然后初始化Flask-Script、Flask-Migrate
和为Python shell定义的上下文。"""