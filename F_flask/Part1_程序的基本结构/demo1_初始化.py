# 所有Flask程序都必须创建一个程序实例
# Web服务器使用（Web Server Gateway Interface, WSGI）协议

# 程序实例是Flask类的对象，一般使用一下代码创建
from flask import Flask
# Flask类的构造函数只有一个必须指定的参数， 即程序主模块或者包的名字，在大多数程序中，Python的__name__变量就是所需的值
app = Flask(__name__)
