#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    forms.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.21   10:04
-------------------------------------------------------------------------------
   @Change:   2020.08.21
-------------------------------------------------------------------------------
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
