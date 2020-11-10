#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'

import unittest
from mydict import Dict


class TestDict(unittest.TestCase):
    def setUp(self):
        print('setup')

    def tearDown(self):
        print('down')

# test

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_keyError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


class Student(object):
    def __init__(self, name, score):  # init后面第一个参数永远是self
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':

    unittest.main()