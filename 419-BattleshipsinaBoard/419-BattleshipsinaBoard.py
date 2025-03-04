class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        res = 0

        def dfs(i,j):
            if i < 0 or i>=m or j<0 or j>=n or board[i][j] == ".":
                return
            
            board[i][j] = "."
            dfs(i+1,j)
            dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    res +=1
                    dfs(i,j)
        return res
