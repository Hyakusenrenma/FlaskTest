from flask_wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired #验证器

class LoginForm(Form):
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=False)