#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

Digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return Digits[s]
    return reduce(fn, map(char2num, s))


def str2float(s):
    Int = s.replace('.', '')
    return str2int(Int) / 10 ** (len(Int) - s.index('.'))


if __name__ == '__main__':
    print(str2float('10.25412315'))
