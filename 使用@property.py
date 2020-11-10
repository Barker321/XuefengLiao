#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'


class Student(object):

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.score = value


class Screen(object):
    def __init__(self, *, width=1, height=1):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise ValueError('width must be int or float')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise ValueError('height must be int or float')
        self.__height = value

    @property
    def resolution(self):
        if (self.width or self.height) is None:
            raise TypeError("you should enroll width or height")
        return self.__width * self.__height


if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)
