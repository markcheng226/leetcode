// Last updated: 3/22/2025, 9:10:21 AM
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        heapq.heappush(self.large,-heapq.heappop(self.small))

        if len(self.small) < len(self.large):
            heapq.heappush(self.small,-heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()