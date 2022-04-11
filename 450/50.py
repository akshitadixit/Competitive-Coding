'''
check if strings are rotations of each other or not
'''

# find index shift of any letter
# shift entire org string by that and compare with new string


def rotationCheck(a, b):
    if len(a) != len(b):
        return False

    temp = a*2
    if b in temp:
        return True
    return False


print(rotationCheck('abcdaabc', 'abcabcda'))
print(rotationCheck('abcdaabc', 'aabcabcda'))
