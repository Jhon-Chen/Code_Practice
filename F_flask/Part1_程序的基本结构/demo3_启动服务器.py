"""程序实例使用run方法启动Flask集成的开发Web服务器"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello world</h1>'


#  __name__ == '__main__' 是python的惯常用法，在这里确保直接执行这个脚本时才启动开发Web服务器
#  如果脚本由其他脚本引入则不会执行
if __name__ == '__main__':
    # 有一些选项参数可以在运行时传入，比如 host=''  port=xxxx，debug是调试模式，在开发过程中一般开启
    app.run(debug=True)
