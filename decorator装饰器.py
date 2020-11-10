#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import time


def log1(func):
    @functools.wraps(func)  # 提前将wrapper函数的名称换成func的名称
    def wrapper(*args, **kwargs):
        print('call: %s' % func.__name__)
        return func(*args, **kwargs)   # 这里一定要加括号，不加括号无法运行该函数
    return wrapper


def log2(text):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s: ' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


def metric(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        beginTime = time.time()
        fn = func(*args, **kwargs)
        endTime = time.time()
        print('%s executed in %s ms' % (func.__name__, (endTime - beginTime)*1000))
        return fn

    return wrapper


@metric
def Time():
    print('now')
    time.sleep(1)


if __name__ == '__main__':
    Time()
    print(Time.__name__)
