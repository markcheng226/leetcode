# Last updated: 10/25/2025, 10:01:41 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq  = [[] for i in range(len(nums)+1)]
        res = []
        count = Counter(nums)

        for num,c in count.items():
            freq[c].append(num)
        
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
