#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     home.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.27   23:21
-------------------------------------------------------------------------------
   @Change:   2020.08.27
-------------------------------------------------------------------------------
"""

from flask import render_template, Blueprint

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    return render_template('index.html')


@home_bp.route('/intro')
def intro():
    return render_template('_intro.html')
