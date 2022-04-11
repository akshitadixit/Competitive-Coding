'''
Check if a string is a valid shuffle of two distinct strings
'''


def checkShuffle(a, b, c):
    if len(c) != len(a)+len(b):
        return False

    if set(c) != set(a).union(set(b)):
        return False

    return True


print(checkShuffle('xy', '12', '1xy2'))
print(checkShuffle('xy', '12', 'y12x'))
print(checkShuffle('xy', '12', 'y21xx'))
