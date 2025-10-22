# Last updated: 10/22/2025, 12:26:04 AM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        res = 0
        room = 0
        i = j = 0

        while i < len(intervals):
            if starts[i] < ends[j]:
                room +=1
                i +=1
                res = max(res,room)
            else:
                room -=1
                j +=1
        return res