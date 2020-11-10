#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""description"""

__author__ = 'WangY'


Path = 'C:\\Users\\Administrator\\Desktop\\123.txt'
with open(Path, 'w', encoding='UTF-8') as f:
    f.write('asd')



from io import StringIO, BytesIO

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO(b'\xe4\xb8\xad')
print(f.read().decode('UTF-8'))