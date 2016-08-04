#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Unit testing of app.py
"""

from unittest import TestCase, main
from unittest.mock import Mock, MagicMock
import app
import json

class TestApp(TestCase):

    def test_index(self):
        # print( dir( app.index() ) )
        self.assertTrue(app.index(), 'Hi!')

    def test_time(self):
        url = 'http://example.com'
        app.request.query['u'] = url

        data = json.loads(app.load_url())

        self.assertTrue(isinstance(data['load_time'], float))
        self.assertTrue(data['load_time'] > 0)

    def test_time_no_url(self):
        app.request.query.clear()
        self.assertEqual(app.load_url(), 'No url given...')

if __name__ == '__main__':
    main()
