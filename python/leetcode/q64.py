class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        # Initialize DP array with the first row's cumulative sums
        dp = [0] * cols
        dp[0] = grid[0][0]
        
        # Fill the first row
        for c in range(1, cols):
            dp[c] = dp[c-1] + grid[0][c]
            
        # Fill the rest of the grid row by row
