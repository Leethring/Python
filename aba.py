#!/usr/bin/env python
# coding=utf-8
def is_palindrame(n):
    s = str(n)
    if s == s[::-1]:
        return int(s)
    else:
        pass
it = filter(is_palindrame,range(1, 1000) )
print('1~1000:', list(it))
