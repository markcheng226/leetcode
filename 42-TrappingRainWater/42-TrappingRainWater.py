# Last updated: 10/26/2025, 4:40:48 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0,len(height)-1
        res = 0
        lmax = height[l]
        rmax = height[r]

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
