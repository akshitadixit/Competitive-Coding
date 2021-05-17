import array as arr
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = arr.array('i',nums)
        d = {}
        for i, x in enumerate(nums):
            t = target-x
            if t not in d:
                d[x] = i
            else:
                return [d[t], i]