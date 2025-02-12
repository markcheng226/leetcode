class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-count,char] for char,count in count.items()]
        heapq.heapify(maxHeap)
        res = []

        while maxHeap:
            count,char = heapq.heappop(maxHeap)
            res+=(char * -count)
        return "".join(res)