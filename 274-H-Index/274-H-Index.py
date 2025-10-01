# Last updated: 9/30/2025, 9:43:40 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        buckets = [0] * (n+1)

        for i in range(len(citations)):
            c = citations[i]
            if c >= n:
                buckets[n] +=1
            else:
                buckets[c] +=1
        
        paper = 0
        for i in range(n,-1,-1):
            paper += buckets[i]
            if paper >= i:
                return i
        return 0