'''
search element in sorted matrix
'''

import numpy as np


def search(arr, k):
    arr = list(np.array(arr).flatten())
    if k in arr:
        return True
    return False
    # or use binary search


print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
