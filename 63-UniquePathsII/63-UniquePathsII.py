class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])

        if (obstacleGrid[0][0] == 1) or (obstacleGrid[m-1][n-1] == 1):
            return 0
        
        obstacleGrid[m-1][n-1] = 1

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r == m-1 and c == n-1:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] =0
                
                else:
                    down = obstacleGrid[r+1][c] if r+1 < m else 0
                    right = obstacleGrid[r][c+1] if c+1 < n else 0
                    obstacleGrid[r][c] = down + right
        return obstacleGrid[0][0]