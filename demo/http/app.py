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

from flask import (
    Flask, redirect, url_for, abort, make_response, request, session
)
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/hi')
def hi():
    return redirect(url_for('hello'))


@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
        respones = '<h1>Hello, %s</h1>' % name
        if 'logged_in' in session:
            respones += '[Authenticated]'
        else:
            respones += '[Not Authenticated]'
    return respones


@app.route('/brew/<drink>')
def teapot(drink):
    if drink == 'coffee':
        abort(418)
    else:
        return 'A drop of tea.'


@app.route('/404')
def not_found():
    abort(404)


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/login')
def login():
    """ simulate login action """
    session['logged_in'] = True
    return redirect(url_for('hello'))


@app.route('/admin')
def admin():
    """ simulate admin management page """
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page.'


@app.route('/logout')
def logout():
    """ simulate user logout """
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True)
