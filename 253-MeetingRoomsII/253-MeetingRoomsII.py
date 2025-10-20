# Last updated: 10/19/2025, 8:22:07 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        i=j=0
        res = 0
        room =0

        while i < len(intervals):
            if starts[i] < ends[j]:
                room +=1
                i +=1
                res = max(res,room)
            else:
                room -=1
                j+=1
        return res