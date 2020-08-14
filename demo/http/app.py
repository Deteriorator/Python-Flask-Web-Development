#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.14   22:18
-------------------------------------------------------------------------------
   @Change:   2020.08.14
-------------------------------------------------------------------------------
"""

from flask import Flask, redirect, url_for, abort

app = Flask(__name__)


@app.route('/hi')
def hi():
    return redirect(url_for('hello'))


@app.route('/hello')
def hello():
    return '<h1>Hello</h1>'


@app.route('/brew/<drink>')
def teapot(drink):
    if drink == 'coffee':
        abort(418)
    else:
        return 'A drop of tea.'


@app.route('/404')
def not_found():
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
