'''
QUICK_SELECT_METHOD
'''
import sys
import time

def kthsmallest(arr, l, r, k):

    # check if k<no.of elements in array
    if k>0 and k<=r-l+1:

        # partition array around last element and get pos of pivot
        pos = partition(arr, l, r)

        # if pos is same as k
        if pos-l == k-1:
            return arr[pos]

        # if pos is greater than k, recur for left subarray
        elif pos-l>k-1:
            return kthsmallest(arr, l, pos-1, k)

        # else recur for right subarray
        return kthsmallest(arr, pos+1, r, k - (pos-l) -1)

    # since k is invalid
    return sys.maxsize

def partition(arr, l, r):

    # typical quick-sort partition algo
    # taking last element as pivot
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            #swap
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

# Driver Code
if __name__ == "__main__":
     
    arr = [12, 3, 5, 7, 4, 19, 26, 1, 33, 50, 77, 43, 10, 27]
    n = len(arr)
    k = 7;
    t0 = time.time()
    print("K'th smallest element is",
           kthsmallest(arr, 0, n - 1, k))
    t1 = time.time()
    arr.sort()
    print(arr[k-1])
    t2 = time.time()
    print(t1-t0)
    print(t2-t1)