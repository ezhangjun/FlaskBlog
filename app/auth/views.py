# coding: UTF-8
from flask import render_template,redirect,request,flash,url_for
from . import auth
from forms import LoginForm,RegistrationForm
from ..models import User
from flask_login import login_user,login_required,logout_user,current_user
from .. import db

@auth.before_app_request
def befor_request():
    if current_user.is_authenticated:
        current_user.ping()



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'邮箱或密码错误')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'你已经退出登录')
    return  redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'注册成功')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)