#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'
from types import MethodType


class Student(object):
    __slots__ = ('age', 'gender')
    pass


def set_age(self, age):
    self.age = age


if __name__ == '__main__':
    s = Student()
    s.set_age = MethodType(set_age, s)   # 给这个实例绑个函数,但是其他实例无法调用这个函数
    Student.set_age = set_age   # 给这个类绑这个函数，对所有实例都有效
    Student.set_age = MethodType(set_age, Student)   # MethodType用法，比较长而且难理解
