# Last updated: 10/19/2025, 9:08:24 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0])

        res = []

        for start,end in intervals:
            if not res or start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1]=max(res[-1][1],end)
        return res