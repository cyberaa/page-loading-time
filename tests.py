#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Unit testing of app.py
"""

from unittest import TestCase, main
from unittest.mock import Mock, MagicMock
import app

class TestApp(TestCase):

    def test_index(self):
        self.assertTrue(app.index(), 'Hi!')

    def test_time(self):
        url = 'http://example.com'
        request = Mock()
        request.query = {'u': url}
        self.assertTrue(app.time(), url)

    def test_time_no_url(self):
        request = Mock()
        request.query = {}
        self.assertTrue(app.time(), 'No url given...')

if __name__ == '__main__':
    main()
