#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Web server
"""

import os
import app
import json

URL_FILE = 'urls.json'

if __name__ == '__main__':
    # Ensure to be in the 
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(URL_FILE):
        with open(URL_FILE) as file:
            app.URLS = json.load(file)
    else:
        app.URLS = ['www.example.com']

    args = {
        'host': os.environ.get('HOST', '0.0.0.0'),
        'port': os.environ.get('HOST', 8080),
        'debug': os.environ.get('HOST', True),
    }
    app.run(**args)
