'''
Given non-negative integer N.
check if N can be expressed as 2^x for some x

N = 2^x
logN = x log2
x = logN/log2
'''
from math import log2


def checkpower(n):
    x = log2(n)  # log of n to the base 2
    if 2**round(x) == n:
        print('YES')
    else:
        print('NO')


def bettercheckpower(n):
    if n & (n-1):
        print('NO')
    else:
        print('YES')


N = int(input())
checkpower(N)
bettercheckpower(N)
