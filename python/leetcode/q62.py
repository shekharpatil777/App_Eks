class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table (m rows, n columns) initialized with 1s.
        # dp[i][j] will store the number of unique paths to reach cell (i, j).
        dp = [[1] * n for _ in range(m)]

        # The first row and first column are initialized to 1 because there is 
        # only one path (all right or all down) to reach any cell in the first row/column.

        # Iterate through the rest of the grid, starting from (1, 1)
        # 
        for i in range(1, m):
            for j in range(1, n):
                # The number of paths to (i, j) is the sum of paths from the 
                # cell above (i-1, j) and the cell to the left (i, j-1).
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
