#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Unit testing of app.helpers
"""

import unittest
import app.helpers


class TestHelpers(unittest.TestCase):

    def test_gather_information(self):
        url = 'http://example.com'
        data = app.helpers.gather_information(url)

        self.assertTrue('loading_time' in data)
        self.assertTrue('page_size' in data)

        self.assertTrue(isinstance(data['loading_time'], float))
        self.assertTrue(data['loading_time'] > 0)
