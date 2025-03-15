class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        ele = []

        for i in range(len(grid)):
            s = sorted(grid[i],reverse = True)
            ele.extend(s[:limits[i]])
        
        ele.sort()
        
        res = 0
        for i in range(k):
            res += ele.pop()
        return res