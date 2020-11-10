#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""python的私有变量"""

__author__ = 'WangY'


class Student(object):
    def __init__(self, *, name, gender, score):
        self.__gender = 'NoData'
        self.__score = 'NoData'
        self.set_score(score)
        self.set_gender(gender)
        self.__name = name

    def print_score(self):
        print('%s %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_gender(self, gender):
        if gender.lower() != ('man' or 'woman'):
            raise ValueError('bad gender')
        else:
            self.__gender = gender.lower()

    def get_gender(self):
        return self.__gender


if __name__ == '__main__':
    Student1 = Student(name='Barker', score=100, gender='Man')
    print(Student1.get_gender())
