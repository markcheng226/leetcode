# Last updated: 7/20/2025, 12:05:20 AM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        pac = set()
        atl = set()
        directions = [1,0],[-1,0],[0,1],[0,-1]

        def dfs(r,c,visited,prev_height):
            if r<0 or c<0 or r>= rows or c>=cols or (r,c) in visited or heights[r][c] < prev_height:
                return
            
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])
        
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result