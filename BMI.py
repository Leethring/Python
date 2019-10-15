#!/usr/bin/env python
# coding=utf-8
height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi < 18.5:
    print('light')
elif bmi < 25:
    print('normal')
elif bmi < 28:
    print('obesity')
elif bim < 32:
    print('too fat')
else:
    print('super fat')

