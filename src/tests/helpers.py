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

        self.assertTrue('timeToLastByte' in data)
        self.assertTrue('bodySize' in data)

        self.assertTrue(isinstance(data['timeToLastByte'], int))
        self.assertTrue(data['timeToLastByte'] > 0)
