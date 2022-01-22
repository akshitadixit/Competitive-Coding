'''
count and say

For example, the saying and conversion for digit string "3322251":
2 3's, 3 2's, 1 5's, 1 1's
= 23+32+15+11
= 23321511

Given a positive integer n, 
return the nth term of the count-and-say sequence.
'''


def say(x):
    if len(x) == 1:
        return '1'

    if len(set(x)) == 1:
        return str(len(x))+x[0]

    # x = '21'
    base = ''
    temp = x[0]
    for y in x[1:]:
        if temp[-1] != y:
            base += str(len(temp))+temp[-1]
            temp = ''
        temp += y
    base += str(len(temp))+temp[-1]

    return base


def countnsay(n):

    if n == 1:
        return 1
    if n == 2:
        return 11

    base = '11'

    while n > 2:
        n -= 1
        base = say(base)
        print(base)

    return base


print(countnsay(10))
