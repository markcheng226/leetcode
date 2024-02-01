class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        time = []

        for start,end in intervals:
            time.append((start,1))
            time.append((end,-1))
        
        time.sort(key=lambda x:(x[0],x[1]))

        count = 0
        max_count = 0

        for t in time:
            count += t[1]
            max_count = max(count,max_count)
        return max_count
        