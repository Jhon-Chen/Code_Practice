"""
Jinja2提供了多种控制结构，可用来改变模板的渲染过程。
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<user>')
def index(user):
    my_list = [4, 5, 9]
    return render_template('demo3_控制结构.html', user=user, list=my_list)


if __name__ == "__main__":
    app.run(debug=True)