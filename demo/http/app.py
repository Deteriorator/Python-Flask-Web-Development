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
from urllib.parse import urlparse, urljoin
from jinja2.utils import generate_lorem_ipsum
from jinja2 import escape
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
    respones = '<h1>Hello, %s</h1>' % escape(name)
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


# redirect to last page
@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)


@app.route('/bar')
def bar():
    return '<h1>Bar page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)


@app.route('/do-something')
def do_something():
    # do something here
    return request_back()


def request_back(defult='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(defult, **kwargs))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)  # 生成两段随机文本
    return '''
    <h1>A very long post</h1>
    <div class="body">%s</div>
    <button id="load">Load More</button>
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.js"></script>
    <script type="text/javascript">
    $(function() {
    $('#load').click(function() {
    $.ajax({
    url: '/more', // 目标URL
    type: 'get', // 请求方法
    success: function(data){ // 返回2XX响应后触发的回调函数
    $('.body').append(data); // 将返回的响应插入到页面中
    }
    })
    })
    })
    </script>''' % post_body


@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)


if __name__ == '__main__':
    app.run(debug=True)
