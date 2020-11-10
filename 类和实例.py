#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""类和实例"""

__author__ = 'WangY'


class Student(object):
    def __init__(self, name, score):  # init后面第一个参数永远是self
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    bart = Student('Barker', 80)
    print(bart.get_grade())
