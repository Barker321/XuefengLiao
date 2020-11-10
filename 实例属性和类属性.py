#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'


class Student(object):
    count = 0   # 类属性，由每个实例所共有

    def __init__(self, name):
        self.name = name
        Student.count += 1   # 对他进行计数,count是每个实例所共有的，所以这里类直接下海干活


if __name__ == '__main__':
    if Student.count != 0:
        print('失败1')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('失败2')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('失败3')
            else:
                print('测试通过')

