'''
Given a row wise sorted matrix of size RxC where 
R and C are always odd, find the median of the matrix.

Expected Time Complexity: O(32 * R * log(C))
Expected Auxiliary Space: O(1)
'''

# {1, 2, 3, 3, 5, 6, 6, 9, 9}
# for median, exactly n/2 ele should be less than median

from bisect import bisect_right as upper_bound
def find_median(arr):
    # binary search in the space 1 - 10^9 or min and max from the arr
    # find a mid that has exactly n//2 numbers less than it
    # for every row use bin search to implement the above
    c = 0


'''
using inbuilt lib called bisect
'''

MAX = 100

# Function to find median in the matrix


def binaryMedian(m, r, d):
    mi = m[0][0]
    mx = 0
    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][d-1] > mx:
            mx = m[i][d-1]

    desired = (r * d + 1) // 2

    while (mi < mx):
        mid = mi + (mx - mi) // 2
        place = [0]

        # Find count of elements smaller than mid
        for i in range(r):
            j = upper_bound(m[i], mid)
            place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    print("Median is", mi)
    return


# Driver code
r, d = 3, 3

m = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
binaryMedian(m, r, d)
