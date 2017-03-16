#  coding: UTF-8
'''
Created on 2017年1月22日

@author: zhangjun
'''
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()
from app import db
print db.Column(db.Integer, primary_key=True)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
    
# class User(db.Model):
#     __tablename__="test"
#     password_hash = db.Column(db.String(128))
#     