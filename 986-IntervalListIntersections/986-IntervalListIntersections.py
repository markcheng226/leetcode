# Last updated: 7/10/2025, 8:26:50 PM
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        res = []

        while i < len(firstList) and j < len(secondList):
            a_start,a_end = firstList[i]
            b_start,b_end = secondList[j]

            max_start = max(a_start,b_start)
            min_end = min(a_end,b_end)

            if max_start <= min_end:
                res.append([max_start,min_end])
            
            if a_end < b_end:
                i+=1
            else:
                j +=1
        return res