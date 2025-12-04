class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        positive_diag = set()  # (row + col)
        negative_diag = set()  # (row - col)
        
        # Initialize board with empty spaces '.'
        board = [["."] * n for _ in range(n)]
        solutions = []

        def backtrack(r):
            # Base Case: All N queens are placed
            if r == n:
                # Format the board and add to solutions
                current_solution = ["".join(row) for row in board]
                solutions.append(current_solution)
                return

            # Try placing a queen in every column 'c' of the current row 'r'
            for c in range(n):
                # Check for conflicts
                if c in cols or (r + c) in positive_diag or (r - c) in negative_diag:
                    continue # Conflict, skip this column

                # Place the Queen and mark the occupied lines
                cols.add(c)
                positive_diag.add(r + c)
                negative_diag.add(r - c)
                board[r][c] = "Q"

                # Recurse to the next row
                backtrack(r + 1)

                # Backtrack: Remove the Queen and unmark the lines
                cols.remove(c)
                positive_diag.remove(r + c)
                negative_diag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return solutions

 
