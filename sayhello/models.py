#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    models.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.21   9:59
-------------------------------------------------------------------------------
   @Change:   2020.08.21
-------------------------------------------------------------------------------
"""

from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
