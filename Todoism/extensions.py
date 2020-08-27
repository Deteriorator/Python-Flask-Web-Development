#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     extensions.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.27   23:19
-------------------------------------------------------------------------------
   @Change:   2020.08.27
-------------------------------------------------------------------------------
"""

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    from Todoism.models import User
    return User.query.get(int(user_id))

