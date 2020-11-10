#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


if __name__ == '__main__':
    obj = MyObject()
    print(hasattr(obj, 'x'))    # 有属性‘x’吗？
    print(setattr(obj, 'y', 12))   # 设定一个属性值y，并赋个值
    print(getattr(obj, 'y', 404))   # 获取这个属性值,如果不存在，就返回后面那个
