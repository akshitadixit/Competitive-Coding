'''
Given an m x n matrix, find all common elements present
in all rows in O(mn) time and one traversal of matrix.
'''


def common(arr):
    hashmap = {}
    for x in arr:
        for y in list(set(x)):
            if y not in hashmap:
                hashmap[y] = 1
            else:
                hashmap[y] += 1

    # for every key in hashmap with freq>no of rows
    return list(filter(lambda x: hashmap[x] == len(arr), hashmap.keys()))


arr = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

print(common(arr))
