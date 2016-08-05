# -*- coding: utf-8 -*-

"""
Unit testing of app.__init__
"""

import unittest
import app


class TestRoutes(unittest.TestCase):

    def test_index(self):
        content = app.index()
        
        for url in app.URLS:
            self.assertTrue(url in content)
