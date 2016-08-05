# -*- coding: utf-8 -*-

"""
Web application
"""

import os
from app.helpers import gather_information
from bottle import run, get, view, request, static_file

URLS = []

@get('/')
@view('index')
def index():
    return dict(urls=URLS)
   

@get('/loadtest')
@view('table')
def loadtest():
    data = []
    for url in URLS:
        data.append(gather_information(url))

    return dict(
        rank_load=sorted(data, key=lambda x: x['timeToLastByte']),
        rank_size=sorted(data, key=lambda x: x['bodySize'])
    )

@get('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')
