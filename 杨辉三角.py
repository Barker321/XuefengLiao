#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def triangles(Max):
    l = [1]
    for i in range(Max):
        yield l
        l = [0] + l + [0]
        l = [l[n] + l[n + 1] for n in range(len(l) - 1)]
    return 'Done'


if __name__ == '__main__':
    for i in triangles(5):
        print(i)
