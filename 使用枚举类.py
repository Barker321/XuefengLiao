#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'
from enum import Enum, unique


@unique   # 帮助我们检查保证没有重复的value值
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self._name = name
        if isinstance(gender, Gender):
            self.gender = gender
        elif isinstance(gender, str):
            if gender.title() in Gender.__members__:
                self.gender = Gender[gender.title()]
            else:
                raise ValueError("请输入正确的字符串")
        else:
            raise ValueError("请输入正确的数据类型")


if __name__ == '__main__':
    bart = Student('Bart', 'maLe')   # 改造成枚举类，以避免使用字符串
    print(bart.gender)
    print(type())