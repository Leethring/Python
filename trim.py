#!/usr/bin/env python
# coding=utf-8
def trim(s):
    if s[0:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-1])
    else:
        return s
if trim('hello   ') != 'hello':
    print('test failed')
elif trim('   hello') != 'hello':
    print('test failed')
elif trim('   hello   ') != 'hello':
    print('test failed')
elif trim ('   hello world   ') != 'hello world':
    print('test failed ')
elif trim (' ') != '':
    print('test failed')
else:
    print('test completed')
