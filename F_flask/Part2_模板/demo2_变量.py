"""Jinja2能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象。比如：
    <p>A value from a dictionary: {{mydict['key']}}.</p>
    <p>A value from a list: {{mylist[3]}}.</p>
    <p>A value from an object's method: {{myobj.somemethod()}}.</p>
可以使用过滤器修改变量，过滤器名添加在变量名之后，中间使用竖线分隔。例如：
    Hello,{{name|capitalize}}
以下是Jinja2中常用的过滤器：
    safe        渲染时不转义
    capitalize      把值得首字母转换成大写，其他字母转换成小写
    lower       把值转换成小写
    upper       把值转换成大写
    title       把值中每个单词的首字母转成大写
    trim        把值首尾的空格去除
    striptags       渲染之前把值中所有的HTML标签都删除
特别说明：默认情况下，处于安全考虑，Jinja2会转义所有变量，很多情况下需要显示变量中存储的HTML代码，就要用到safe过滤器
    """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    mydict = {'key': 'abc',
              'you': 250}
    my_list = [1, 2, 39, 123]
    return render_template('demo2_变量及过滤器.html', mydict=mydict, mylist=my_list)


if __name__ == "__main__":
    app.run(debug=True)