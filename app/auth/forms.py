# coding: UTF-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email,Regexp,ValidationError,EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1,64),
                                           Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'记住密码')
    submit = SubmitField(u'登录')

class RegistrationForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64),
                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                    u'用户名只能是字母、数字、点、下划线')])
    password = PasswordField(u'密码', validators=[Required(),
                                                EqualTo('password2', message=u'两次密码必须相同')])
    password2 = PasswordField(u'确认密码', validators=[Required()])

    submit = SubmitField(u'注册')

    def validate_email(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(u'邮箱已经存在')

    def validate_username(self, value):
        if User.query.filter_by(username=value.data).first():
            raise  ValidationError(u'用户名已存在')
