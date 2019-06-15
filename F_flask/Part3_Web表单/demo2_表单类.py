"""使用WTF时，每个Web表单都由一个继承自 Form 的类表示。这个类定义表单中的一组字段，每个字段都用对象表示。
字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入值是否符合要求。"""
from flask import Flask
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)


# 表单中的字段都定义为类变量，类变量的值是相应字段类型的对象
class NameForm(Form):
    # StringField 类表示属性为 type="text" 的 <input> 元素
    # SubmitField 类表示属性为 type="submit" 的 <input> 元素
    # 表单构造的第一个参数是把表单渲染成HTML时使用的标号
    name = StringField("What's your name?", validators=[Required()])
    # StringField 构造函数中的可选参数 validators 指定一个由验证函数组成的列表，在接受用户提交的数据之前验证数据。
    # 验证函数 Required() 确保提交的字段不能为空
    submit = SubmitField('Submit')

    """
    WTForm 支持的 HTML字段：
    StringField             文本字段
    TextAreaField           多行文本字段
    PasswordField           密码文本字段
    HiddenField             隐藏文本字段
    DateField               文本字段，值为 datetime.date 格式
    DateTimeField           文本字段，值为 datetime.datetime格式
    IntegerField            文本字段，值为整数
    DecimalField            文本字段，值为 decimal.Decimal
    FloatField              文本字段，值为浮点数
    BooleanField            复选框，值为 True 和 False
    RadioField              一组单选框
    SelectField             下拉列表
    SelectMultipleField     下拉列表，可选择多个值
    FileField               文件上传字段
    SubmitField             表单提交按钮
    FormField               把表单作为字段嵌入另一个表单
    FieldList               一组指定类型的字段
    """

    """WTForm验证函数：
    Email                   验证电子邮件地址
    EqualTo                 比较两个字段的值，常用于要求输入两次密码确认的场合
    IPAddress               验证IPv4网络地址
    Length                  验证输入字符串的长度
    NumberRange             验证输入的值在数字范围内
    Optional                无输入值时跳过其他验证函数
    Required                确保字段中有数据
    Regexp                  使用正则表达式验证输入值
    URL                     验证URL
    AnyOf                   确保输入值在可选值列表中
    NoneOf                  确保输入值不在可选值列表中
    """


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)
