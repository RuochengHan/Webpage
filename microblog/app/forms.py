from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from markupsafe import Markup

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  #submit_value = Markup('<span class="oi oi-check" title="Submit"></span>')
  #submit = SubmitField(submit_value)


class PostForm(FlaskForm):
  post = TextAreaField('Title', validators=[
    DataRequired(), Length(min=1, max=140)])
  #submit = SubmitField('Submit')
