#  coding: UTF-8
'''
Created on 2017年1月22日

@author: zhangjun
'''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash=db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError(u'password不是一个可读的属性')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return  check_password_hash(self.password_hash,password)
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
