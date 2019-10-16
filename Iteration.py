#!/usr/bin/env python
# coding=utf-8
def findMinAndMax(L):
    if L == []:
        return(None, None)
    else:
        max=L[0]
        min=L[0]
        for i in L:
            if i > max:
                max=i
            if i < min:
                min = i
        return(min, max)
if findMinAndMax([]) != (None, None):
    print('test faile1')
elif findMinAndMax([7]) != (7, 7):
    print('test faile2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('test faile3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1,9):
    print('test faled')
else:
    print('test completed')
