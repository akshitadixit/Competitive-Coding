from itertools import permutations
from math import factorial

s = input()

ctr = 0


def words(letters):
    for n in range(1, len(letters)+1):
        yield from map(''.join, permutations(letters, n))


print(len(set(words(s))) % 998244353)
