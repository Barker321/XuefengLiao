#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def prod(L):
    def Multxy(x, y):
        return x * y
    return reduce(Multxy, L)


if __name__ == '__main__':
    print(prod([3, 5, 7, 9]))