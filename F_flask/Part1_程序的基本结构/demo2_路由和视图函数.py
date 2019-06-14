""" 客户端把请求发送给Web服务器，web服务器再把请求发送给Flask程序实例。
程序实例需要知道每个URL请求运行哪些代码，所以保存了一个URL到Python函数的映射关系，这种映射关系就称之为路由"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
# 这样的函数称为视图函数 这个函数的返回值称为“响应”
def index():
    return '<h1>Hello World!</h1>'


# Flask支持这种动态的URL，尖括号里是动态部分，任何能匹配静态部分的URL都会映射到这个路由上
# 调用视图函数时，Flask会将动态部分作为参数传入函数
@app.route('/user/<name>')
def user(name):
    # 路由中的动态部分默认使用字符串，不过也可以使用类型定义，例如：/user/<int:id> 只会匹配动态片段id为整数的URL
    # Flask支持在路由中使用int、float、和path类型。path也是字符串类型，但不把斜线视作分隔符，而将其当做动态片段的一部分
    return '<h1>Hello %s</h1>'
