#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    print(list(filter(is_palindrome, range(1, 1000))))
