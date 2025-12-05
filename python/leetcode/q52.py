class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Sets to track occupied columns and diagonals in O(1) time
        cols = set()
        pos_diag = set() # (r + c) is constant
        neg_diag = set() # (r - c) is constant

        # List to store all valid board configurations
        res = []

        # Current board state: stores the column 'c' where the queen is placed for each row 'r'
        board = ["." * n for _ in range(n)]

        def backtrack(r):
            # Base Case: All N queens have been placed successfully
            if r == n:
                res.append(list(board))
                return

            for c in range(n):
                # Check for conflicts in column, positive diagonal, and negative diagonal
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # 1. Place the queen (mark as occupied)
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Update the board string for the current row
                # e.g., for n=4, c=1, board[r] becomes ".Q.."
                board[r] = board[r][:c] + "Q" + board[r][c+1:]

                # 2. Recurse to the next row
                backtrack(r + 1)

                # 3. Backtrack (unmark and reset board)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
                # Reset the board string for the current row to empty
                board[r] = "." * n

        backtrack(0)
        return res