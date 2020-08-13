#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.14   0:09
-------------------------------------------------------------------------------
   @Change:   2020.08.14
-------------------------------------------------------------------------------
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello Flask!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
