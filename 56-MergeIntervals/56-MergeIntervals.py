# Last updated: 10/19/2025, 9:42:42 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        res = []

        intervals.sort(key=lambda x:x[0])

        

        for start,end in intervals:
            if not res or start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1] = max(res[-1][1],end)
        
        return res