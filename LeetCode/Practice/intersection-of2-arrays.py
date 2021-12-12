#    Possible better approach:
#    Use collections.Counter .
#    Use the fact that dict1.keys() & dict2.keys() returns the keys common to dict1 and dict2

'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        c3 = c1 & c2
        return list(c3.elements())
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        
        def search(arr, val):
            hi = len(arr)-1
            lo=0
            while lo<=hi:
                mid = (lo+hi)//2
                if arr[mid]==val:
                    return (1,mid)
                elif arr[mid]<val:
                    lo=mid+1
                else:
                    hi=mid-1
            return (0,-1)
        
        ans = []
        for x in nums1:
            flag, pos = search(nums2, x)
            if flag:
                del nums2[pos]
                ans.append(x)
        return ans