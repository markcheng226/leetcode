# Last updated: 10/21/2025, 11:32:06 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        i=0

        while i < len(intervals):
            if intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
                i+=1
            else:
                break

        while i < len(intervals):
            if intervals[i][0] <=newInterval[1]:
                newInterval[0] = min(intervals[i][0],newInterval[0])
                newInterval[1] = max(intervals[i][1],newInterval[1])
                i +=1
            else:
                break
        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i +=1
        
        return res
