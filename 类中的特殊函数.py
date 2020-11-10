#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):   # 迭代
        return self

    def __next__(self):   # 迭代器的next
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):   # 想List那样取出元素
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start and ((x - start) % step) == 0:
                    L.append(a)
                a, b = b, a + b
            return L


class Student(object):
    def __init__(self, name):
        self._name = name

    def __getattr__(self, item):   # 如果调用没有定义过的属性，就会寻找这个函数
        if item == 'score':
            return lambda: 25

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self._name)


class Chain(object):   # 调用API

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def users(self, user):
        return Chain('%s/%s' % (self._path, user))


if __name__ == '__main__':
    # for n in Fib():
    #     print(n)
    print(Chain().asd.sd.users('djsi').asif.asid)
    M = Student('Michael')
    print(M.score())
