# Last updated: 10/22/2025, 12:07:01 AM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort(key=lambda x:x[0])

        prev_end = intervals[0][1]

        for start,end in intervals[1:]:
            if start < prev_end:
                res +=1
                prev_end = min(end,prev_end)
            else:
                prev_end = end
        return res