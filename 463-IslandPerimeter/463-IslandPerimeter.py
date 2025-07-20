# Last updated: 7/19/2025, 10:20:16 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        directions = [1,0],[-1,0],[0,1],[0,-1]

        def dfs(r,c):
            if r < 0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0:
                return 1
            
            if (r,c) in visited:
                return 0
                
            res =0
            visited.add((r,c))
            for dr,dc in directions:
                res += dfs(r+dr,c+dc)
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c)
        return 0