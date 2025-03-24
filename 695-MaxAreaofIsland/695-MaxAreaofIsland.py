# Last updated: 3/24/2025, 11:14:15 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        directions = [1,0],[-1,0],[0,1],[0,-1]
        
        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0 or(r,c) in visit):
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr,dc in directions:
                area += dfs(r+dr,c+dc)
            return area

        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area,dfs(r,c))
        return area