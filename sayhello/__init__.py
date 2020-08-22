#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    __init__.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.21   9:50
-------------------------------------------------------------------------------
   @Change:   2020.08.21
-------------------------------------------------------------------------------
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
moment = Moment(app)

from sayhello import views, errors, commands
