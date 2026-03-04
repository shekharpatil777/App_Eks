class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Check bounds and if the cell is an 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark as 'Safe'
            board[r][c] = 'S'
            
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Traverse the border to find non-surrounded regions
        for r in range(rows):
            dfs(r, 0)            # Left border
            dfs(r, cols - 1)     # Right border
            
        for c in range(cols):
            dfs(0, c)            # Top border
            dfs(rows - 1, c)     # Bottom border

        # 2. Re-map the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Surrounded -> Captured
                elif board[r][c] == 'S':
                    board[r][c] = 'O'  # Safe -> Restored