#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def normalize(name):
    def inf(a):
        if 65 <= ord(a) <= 90:
            upper_a = ord(a) + 32
            return chr(upper_a)
        else:
            return a
    name = list(map(inf, name))
    if ord('a') <= ord(name[0]) <= ord('z'):
        name[0] = chr(ord(name[0]) - 32)
    return ''.join(name)


if __name__ == '__main__':
    print(normalize(''))