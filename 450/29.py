'''
Given an array arr of size n and an integer X. 
Find if there's a triplet in the array which sums 
up to the given integer X. 
'''


def duplet(arr, k):
    for x in arr:
        if k-x in arr:
            return [x, k-x]
    return 0


def triplet(arr, k):
    hashmap = []
    for x in arr:
        pair = duplet(arr, k-x)
        if pair:
            hashmap.append([pair[0], pair[1], x])
    if hashmap:
        print(hashmap)
        return True
    return False


arr = [12, 3, 4, 1, 6, 9]
print(triplet(arr, 24))
