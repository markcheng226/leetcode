# Last updated: 10/19/2025, 8:37:46 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[0])
        res = 0
        prev_end = intervals[0][1]

        for start,end in intervals[1:]:
            if start < prev_end:
                res +=1
                prev_end = min(prev_end,end)
            else:
                prev_end = end
        return res