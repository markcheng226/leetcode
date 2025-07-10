# Last updated: 7/9/2025, 10:02:53 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        lmax = height[l]
        rmax = height[r]
        res = 0

        while l < r:
            if lmax < rmax:
                l+=1
                lmax = max(lmax,height[l])
                res += lmax - height[l]
            else:
                r -=1
                rmax = max(rmax,height[r])
                res += rmax - height[r]
        return res