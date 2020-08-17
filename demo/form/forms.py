#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     forms.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.17   23:23
-------------------------------------------------------------------------------
   @Change:   2020.08.17
-------------------------------------------------------------------------------
"""
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField,TextAreaField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')
