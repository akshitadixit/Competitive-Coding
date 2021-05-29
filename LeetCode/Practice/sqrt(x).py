class Solution:
    def mySqrt(self, x: int) -> int:
        hi = x
        lo = 0
        mid = 1
        while lo<=hi:
            mid = (lo+hi)//2
            sq = mid**2
            if sq>x:
                hi=mid-1
            elif sq<x:
                lo=mid+1
            else:
                return int(mid)
                
        return int(hi) #since we're rounding down and hi is the value to the left of where the loop breaks