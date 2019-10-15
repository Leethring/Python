#!/usr/bin/env python
# coding=utf-8
import math
def quadratic(a, b, c,):
    delta = b * b - 4 * a * c
    x1 = (- b + math.sqrt(delta) )/(2 * a)
    x2 = (- b - math.sqrt(delta) )/(2 * a)
    return x1, x2
print('get the resolution of the formulation ax^2+bx+c=0')
a = input('a = ')
b = input('b = ')
c = input('c = ')
e = float(a)
f = float(b)
g = float(c)
delta = f * f - 4 * e * g
if delta < 0:
    print('no result')
else:
    x = quadratic(e, f, g)
    print(x)
# test
print('quadratic(2, 3, 1 ) = ', quadratic(2, 3, 1))
print('quadratic(1, 3, -4 ) = ', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('text failed')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('test failed')
else:
    print('we did it ')

