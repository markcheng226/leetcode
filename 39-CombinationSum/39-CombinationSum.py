# Last updated: 10/22/2025, 12:31:09 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            for j in range(i, len(candidates)):
                if candidates[j] > remain:
                    break
                cur.append(candidates[j])
                backtrack(j, cur, remain - candidates[j])
                cur.pop()
        
        backtrack(0, [], target)
        return res