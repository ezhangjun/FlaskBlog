# coding: UTF-8
'''
Created on 2017年1月22日

@author: zhangjun
'''
from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
# from .forms import NameForm
from .. import db

# from ..models import User
@main.route('/', methods=['GET', 'POST'])
def index():

    return render_template('user.html')