'''
Given an array of N integers, and an integer K, find the
number of pairs of elements in the array whose sum is equal to K.
'''


def pairs_with_sum(arr, k):
    # the seen vs [x, k-x] won't work in case there are more
    # than one occurences of certain numbers or when x-k = x

    # hence we keep a map
    freq = {}
    ctr = 0
    for x in arr:
        if k-x in freq:
            ctr += freq[k-x]

    # by the time we add the 4th '1', we have added 1+2+3 into ctr
    # makes sense

        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1

    return ctr


arr = [1, 1, 1, 1]
print(pairs_with_sum(arr, 2))
