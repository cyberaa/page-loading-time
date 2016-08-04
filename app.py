#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Web application
"""

from bottle import run, get, view, request
import json
import os
from time import time
import urllib.request
from helpers import gather_information


@get('/')
@view('index')
def index():
    data = []
    for url in URLS:
        data.append(gather_information(url))

    return dict(
        rank_load=sorted(data, key=lambda x: x['loading_time']),
        rank_size=sorted(data, key=lambda x: x['page_size'])
    )


if __name__ == '__main__':
    if os.path.exists('urls.json'):
        with open('urls.json') as file:
            URLS = json.load(file)
    else:
        URLS = ['www.example.com']

    args = {
        'host': os.environ.get('HOST', '0.0.0.0'),
        'port': os.environ.get('HOST', 8080),
        'debug': os.environ.get('HOST', True),
    }
    run(**args)
