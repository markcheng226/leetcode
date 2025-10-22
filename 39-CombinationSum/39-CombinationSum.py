# Last updated: 10/22/2025, 12:30:11 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()

        def backtrack(i,cur,total):
            if total == target:
                res.append(cur.copy())
            
            for j in range(i,len(candidates)):
                if total + candidates[j] > target:
                    break
                else:
                    cur.append(candidates[j])
                    backtrack(j,cur,total +candidates[j])
                    cur.pop()
        backtrack(0,[],0)
        return res