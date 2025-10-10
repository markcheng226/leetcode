# Last updated: 10/10/2025, 1:12:56 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        cnt = Counter(nums)
        res = []

        for num,c in cnt.items():
            freq[c].append(num)
        
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res