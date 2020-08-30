#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     utils.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.30   23:20
-------------------------------------------------------------------------------
   @Change:   2020.08.30
-------------------------------------------------------------------------------
"""

from flask import flash


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error)
                  )

