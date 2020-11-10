#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

def count():
    fs = []

    def f(I):
        return lambda: I*I

    for i in range(1, 4):
        fs.append(f(i))
    return fs


def createCounter():
    j = 0

    def counter():
        nonlocal j
        j = j + 1
        return j

    return counter


if __name__ == '__main__':
    f1, f2, f3 = count()
    print(f1, f2(), f3())
