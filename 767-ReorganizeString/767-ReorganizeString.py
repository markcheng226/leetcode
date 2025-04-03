# Last updated: 4/3/2025, 2:54:47 PM
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-count,char] for char, count in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            
            count,char = heapq.heappop(maxHeap)
            res += char
            count +=1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            
            if count != 0:
                prev = [count,char]
        return res
            
            