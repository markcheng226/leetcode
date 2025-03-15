class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxHeap = []

        for i in range(len(grid)):
            row = sorted(grid[i],reverse = True)
            top = (row[:limits[i]])
            for val in top:
                heapq.heappush(maxHeap,-val)
    
    
        res = 0
        for i in range(k):
            res -= heapq.heappop(maxHeap)
        return res