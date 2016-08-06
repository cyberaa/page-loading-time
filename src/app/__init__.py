# -*- coding: utf-8 -*-

"""
Web application
"""

import os
from app.helpers import gather_information
from bottle import run, get, view, static_file

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
        rank_load=sorted(data, key=lambda x: x['loading_time']),
        rank_size=sorted(data, key=lambda x: x['page_size'])
    )


@get('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')
