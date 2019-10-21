#!/usr/bin/env python
# coding=utf-8
from functools import reduce
def normalize(name):
    return str.title(name)
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize , L1))
print(L2)

def prod(L):
    def multiply(x,y):
        return x*y
    return reduce(multiply,L)
print('3*5*7*9 = ', prod([3,5,7,9]))
if prod([3,5,7,9]) == 945:
    print('test finish')
else:
    print('test failed')

def fn(x,y):
    return x*10 +y
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]
def str2float(s):
    L = s.split(sep='.')
    return reduce(fn, map(char2num,L[0]))+reduce(fn,map(char2num,L[1]))/(10**(len(s)-s.index('.')-1))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('test finish')
else:
    print('test faild')
