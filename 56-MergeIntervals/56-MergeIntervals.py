# Last updated: 10/22/2025, 12:00:27 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        res = []

        intervals.sort(key=lambda x:x[0])
    
        for start,end in intervals:
            if not res:
                res.append([start,end])
            elif start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1] = max(end,res[-1][1])
        return res