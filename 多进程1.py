#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'
import os
from multiprocessing import Process


def run_prpc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_prpc, args=('test',))
    print('Child process will start')
    p.start()   # 使该进程运行
    p.join()    # 等待该进程运行完毕
    print('child process end')