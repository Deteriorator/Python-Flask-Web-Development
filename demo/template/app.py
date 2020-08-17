#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.16   22:58
-------------------------------------------------------------------------------
   @Change:   2020.08.16
-------------------------------------------------------------------------------
"""

import os
from flask import Flask, render_template, flash, redirect, url_for, Markup

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)


@app.context_processor
def inject_foo():
    foo = 'I am foo.'
    return dict(foo=foo)


"""
def inject_foo():
    foo = 'I am foo.'
    return dict(foo=foo)
app.context_processor(inject_foo)

app.context_processor(lambda: dict(foo='I am foo.'))
"""


@app.template_global()
def bar():
    return 'I an bar'


"""
app.add_template_global（your_global_function）
"""


@app.route('/hello')
def hello():
    text = Markup('<h1>Hello, Flask!</h1>')
    return render_template('index.html', text=text)


@app.template_filter()
def musical(s):
    """ user define filter """
    return s + Markup(' &#9835;')


@app.template_test()
def baz(n):
    """ a user define template test """
    if n == 'baz':
        return True
    return False


if __name__ == '__main__':
    app.run(debug=True)
