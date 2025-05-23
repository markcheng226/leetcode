# Last updated: 3/23/2025, 7:48:50 PM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i : [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        cycle = set()
        visit = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
