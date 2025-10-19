# Last updated: 10/19/2025, 7:34:27 PM
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        
        prev_end = float("-inf")
        for start,end in intervals:
            if start < prev_end:
                return False
            else:
                prev_end = end
        return True