#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'
import pickle


# d = dict(name='Bob')
# with open("C:\\Users\\Administrator\\Desktop\\123.txt", 'wb') as f:
#     pickle.dump(d, f)
with open("C:\\Users\\Administrator\\Desktop\\123.txt", 'rb') as f:
    d = pickle.load(f)

print(d)