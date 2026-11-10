class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        m, n = len(board), len(board[0])
        count = 0
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    # Skip if it is part of a battleship extending from above
                    if r > 0 and board[r - 1][c] == 'X':
