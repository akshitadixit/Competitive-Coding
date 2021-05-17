import array as arr
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = arr.array('i',sorted(nums1 + nums2))
        if not len(s)%2 == 0:
            return s[int(len(s)/2)]
        else:
            return (s[int(len(s)/2) - 1] + s[int(len(s)/2)]) / 2