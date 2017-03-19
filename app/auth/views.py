# coding: UTF-8
from flask import render_template,redirect,request,flash,url_for
from . import auth
from forms import LoginForm
from ..models import User
from flask_login import login_user

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

