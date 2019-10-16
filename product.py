#!/usr/bin/env python
# coding=utf-8
def product(*numbers:int):
    if len (numbers) ==0:
        raise TypeError
    i = 1 
    for n in numbers:
        i = i * n
    return i
print('product(5) =', product(5))
print('product(5, 6) =', product(5,6))
print('product(5,6,7)= ', product(5,6,7))
print('product(5, 6, 7, 9)= ', product(5, 6, 7, 9))
if product(5) != 5:
    print('test failed')
elif product(5, 6) != 30:
    print('text failed')
elif product(5, 6, 7) != 210:
    print('test faile')
elif product(5, 6, 7, 9) != 1890:
    print('text failed')
else:
    try:
        product()
        print('teet failed')
    except TypeError:
        print('test finish')

