class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # To ensure we don't reuse the same cell

        def dfs(r, c, i):
            # Base Case: If we've matched every letter in the word
            if i == len(word):
                return True
            
            # Check boundaries, wrong character, or if cell already visited
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # Mark the current cell as visited
            path.add((r, c))
            
            # Explore all 4 adjacent directions (Up, Down, Left, Right)
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack: Remove the cell from path so it can be used in other branches
            path.remove((r, c))
            return res

       # Kick off the search from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False 