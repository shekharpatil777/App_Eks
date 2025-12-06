class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        
        # Arrays to track attacked columns, main diagonals, and anti-diagonals
        # Note: Diagonals need size 2*n - 1
        self.cols = [False] * n
        self.diag1 = [False] * (2 * n - 1)  # row + col
        self.diag2 = [False] * (2 * n - 1)  # row - col + (n - 1)

        self.dfs(0, n)
        return self.ans

    def dfs(self, row: int, n: int) -> None:
        # Base case: All N queens have been placed successfully
        if row == n:
            self.ans += 1
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            
            # Calculate diagonal indices
            diag1_idx = row + col
            diag2_idx = row - col + (n - 1)

            # Check if position (row, col) is safe
            if not self.cols[col] and not self.diag1[diag1_idx] and not self.diag2[diag2_idx]:
                
                # Place the queen (Mark attack zones)
                self.cols[col] = True
                self.diag1[diag1_idx] = True
                self.diag2[diag2_idx] = True

                # Recurse to the next row
                self.dfs(row + 1, n)

