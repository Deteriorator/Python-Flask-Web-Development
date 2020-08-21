#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    settings.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.21   9:50
-------------------------------------------------------------------------------
   @Change:   2020.08.21
-------------------------------------------------------------------------------
"""

import os
import sys

from sayhello import app

# sqlite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

dev_db = prefix + os.path.join(app.root_path, 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
