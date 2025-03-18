class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:


        maxHeap = []
        for i in range(len(grid)):
            sortedRow = sorted(grid[i],reverse = True)
            topValue = sortedRow[:limits[i]]

            for val in topValue:
                heapq.heappush(maxHeap,-val)
        res = 0
        for i in range(k):
            res += -heapq.heappop(maxHeap)
        return res