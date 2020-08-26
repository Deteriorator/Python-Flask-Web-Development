# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     utils.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.26   22:04
-------------------------------------------------------------------------------
   @Change:   2020.08.26
-------------------------------------------------------------------------------
"""

try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from flask import request, redirect, url_for


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))
