#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'

import os
import shutil

# print(os.environ.get('x', '你啥也没看到'))  # 获取某个环境变量的值，在右上角可以看到环境变量的某些值，可以在环境变量里存放密码等一些不方便被看到的东西
# print(os.path.abspath('.'))  # 查看当前文件目录的绝对路径
# # 在某个目录下创建一个新目录
# os.path.join('X:\\', 'test')  # 首先把新目录的完整路径表示出来
# os.makedirs('X:\\test')
# os.rmdir('X:\\test')
#
# a = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']
# print(a)


def search(name, path='.'):
    for Dir in os.listdir(path):
        if name in Dir:
            return os.path.join(path, Dir)
        if os.path.isdir(os.path.join(path, Dir)):
            New_path = os.path.join(path, Dir)
            a = search(name, New_path)
            if a is not None:
                return a


if __name__ == '__main__':
    print(search('init.tcl'))