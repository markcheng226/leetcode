# Last updated: 10/19/2025, 7:42:16 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        i=j=0
        room = res = 0
        
        while i < len(intervals):
            if starts[i] < ends[j]:
                room +=1
                res = max(res,room)
                i +=1
            else:
                room -=1
                j +=1
        return res