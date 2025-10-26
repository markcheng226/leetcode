# Last updated: 10/26/2025, 3:21:59 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                x = board[r][c]

                if x == ".":
                    continue
                if x in rows[r] or x in cols[c] or x in squares[(r//3),(c//3)]:
                    return False
                
                rows[r].add(x)
                cols[c].add(x)
                squares[(r//3),(c//3)].add(x)
        return True