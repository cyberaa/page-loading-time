#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Web application
"""

from bottle import route, get, post, run, request, template
import json

@get('/')
def index():
    return 'Hi!'

@get('/time')
def time():
    if not 'u' in request.query:
        return 'No url given...'

    # return json.dumps(browser.title, indent=2, separators=(',', ': '))
    return request.query['u']

if __name__ == '__main__':
    run()
