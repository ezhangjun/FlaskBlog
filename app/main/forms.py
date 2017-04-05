# coding: UTF-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import Required, Length, Email,Regexp,ValidationError,EqualTo
from flask_pagedown.fields import PageDownField
from ..models import User

class EditProfileForm(Form):
    name = StringField(u'真实姓名', validators=[Length(0, 64)])
    location = StringField(u'地址', validators=[Length(0, 64)])
    about_me = TextAreaField(u'关于我')
    submit = SubmitField(u'提交')


class PostForm(Form):
    body = PageDownField(u"内容", validators=[Required()])
    submit = SubmitField(u'提交')

class CommentForm(Form):
    body = PageDownField(u"", validators=[Required()])
    submit = SubmitField(u'提交')