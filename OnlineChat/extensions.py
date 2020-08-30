#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     extensions.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.30   23:18
-------------------------------------------------------------------------------
   @Change:   2020.08.30
-------------------------------------------------------------------------------
"""

from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
moment = Moment()


@login_manager.user_loader
def load_user(user_id):
    from OnlineChat.models import User
    return User.query.get(int(user_id))


login_manager.login_view = 'auth.login'
