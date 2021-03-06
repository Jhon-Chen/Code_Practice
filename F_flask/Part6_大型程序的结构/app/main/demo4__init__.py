from flask import Blueprint
from . import views, errors

main = Blueprint('main', __name__)


"""转换成程序工厂函数的操作让定义路由变得复杂了。在单脚本程序中，程序实例存在于全局作用域中，路由可以直接使用app.route修饰器定义。
但现在程序在运行时创建，只有调用create_app()之后才能使用app.route修饰器，这时定义路由就太晚了。和路由一样，自定义错误页面处理程序
也面临相同的困难，因为错误页面处理程序使用app.errorhandler修饰器定义。"""
"""幸好Flask使用蓝本提供了更好的解决方法。蓝本和程序类似，也可以定义路由。不同的是，在蓝本中定义的路由处于休眠状态，知道蓝本注册
到程序上后，路由才真正成为程序的一部分。使用位于全局作用域中的蓝本时，定义路由的方法几乎和单脚本一样。
和程序一样，蓝本可以在单个文件中定义，也可使用更结构化的方式在包中的多个模块中创建。为了获得最大的灵活性，程序包中创建一个子包，用
于保存蓝本。"""

# app/main/__init__.py:创建蓝本

"""通过实例化一个Blueprint类对象可以创建蓝本。这个构造函数有两个必须指定的参数：蓝本的名字和蓝本所在的包或模块。和程序一样，大多
数情况下第二个参数使用Python的__name__变量即可。
程序的路由保存在包里的 app/main/views.py 模块中，而错误处理程序保存在 app/main/errors.py 模块中。导入这两个模块就能把路由和错误
处理程序与蓝本联系起来。注意，这些模块在 app/main/__init__.py 脚本的末尾导入，这是为了避免循环导入依赖，因为在views.py和
errors.py中还要导入蓝本main。"""

# 注册蓝本见: demo3, app/__init__.py