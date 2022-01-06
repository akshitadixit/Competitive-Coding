'''
Given an integer array of size n,
find all elements that appear more than ⌊ n/3 ⌋ or k times.
'''

def majority(arr, k):
    freq = {}
    for x in arr:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    
    for x in freq:
        if freq[x]<k:
            del arr[]