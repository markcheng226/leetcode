# Last updated: 10/11/2025, 11:03:22 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0, len(height)-1

        res = 0

        while l < r:
            area = min(height[l],height[r]) * (r-l)
            res = max(res,area)

            if height[l] < height[r]:
                l +=1
            else:
                r-=1
        
        return res