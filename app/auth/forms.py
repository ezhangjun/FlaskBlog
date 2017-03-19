# coding: UTF-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1,64),
                                           Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'记住密码')
    submit = SubmitField(u'登录')

