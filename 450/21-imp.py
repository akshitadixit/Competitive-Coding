'''
merge intervals
time: nlogn
space: logn or n
'''


def merge_intervals(arr):
    res = []
    arr.sort()
    for x in arr:
        # either res is empty or last inserted element does not overlap
        if not res or res[-1][1] < x[0]:
            res.append(x)
        else:
            # maz=ximize last inserted intervals
            res[-1][1] = max(res[-1][1], x[1])
