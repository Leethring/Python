#!/usr/bin/env python
# coding=utf-8
sum = 0 
for x in range(101):
    sum = sum + x
print(sum)
sums = 0 
n = 99
while n > 0:
    sums = sums + n
    n = n - 2
print(sums)
s = 1 
while s <= 100:
    if s > 10: 
        break
    print(s)
    s = s + 1
print('END')
a = 0 
while a < 10 :
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
