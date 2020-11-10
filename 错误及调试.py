#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'
from functools import reduce


def str2num(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: x + acc, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345=', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6=', r)


main()
