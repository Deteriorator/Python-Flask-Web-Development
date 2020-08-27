#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     settings.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.27   23:19
-------------------------------------------------------------------------------
   @Change:   2020.08.27
-------------------------------------------------------------------------------
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    TODOISM_ITEM_PER_PAGE = 20

    SECRET_KEY = os.getenv('SECRET_KEY', 'a secret string')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data.db'))
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
