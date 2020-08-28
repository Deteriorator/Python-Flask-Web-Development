#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     settings.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.28   23:56
-------------------------------------------------------------------------------
   @Change:   2020.08.28
-------------------------------------------------------------------------------
"""

import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig:
    CATCHAT_MESSAGE_PER_PAGE = 30
    CATCHAT_ADMIN_EMAIL = os.getenv('CATCHAT_ADMIN_EMAIL', 'admin@helloflask.com')

    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
