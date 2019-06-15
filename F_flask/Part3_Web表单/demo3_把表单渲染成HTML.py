from flask import Flask
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
app = Flask(__name__)


class NameForm(Form):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/')
def index():

    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)