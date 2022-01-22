'''
Check if a string is a valid shuffle of two other strings

1. check for all chars in s1 and s2 if they be in base
2. 
'''


def check_shuffle(base, s1, s2):
    for s in base:
        if len(s1)+len(s2) == len(base):
            if s in s1 or s in s2:
                continue
            else:
                return -1
        else:
            return -1
    return 1
