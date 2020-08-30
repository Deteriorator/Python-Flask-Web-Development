#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     wsgi.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.30   23:25
-------------------------------------------------------------------------------
   @Change:   2020.08.30
-------------------------------------------------------------------------------
"""

from OnlineChat import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
