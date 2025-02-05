class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [ [] for i in range(len(nums)+1)]
        count = Counter(nums)

        for num,count in count.items():
            freq[count].append(num)

        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
