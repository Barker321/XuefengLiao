#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    f = lambda n: n % 2 == 1
    L = list(filter(f, range(1, 20)))
    print(f(3))
    print(L)
