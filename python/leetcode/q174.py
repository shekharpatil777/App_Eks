class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        
        # Create a DP table initialized with infinity
        # We add an extra row and column to handle boundaries easily
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        
        # Base cases: health needed after reaching the princess is 1
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1
        
        # Fill the table backwards
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                # Health needed to survive the next step
                min_health_needed = min(dp[r + 1][c], dp[r][c + 1])
                
                # Health needed before entering current cell
                dp[r][c] = max(1, min_health_needed - dungeon[r][c])
        
        return dp[0][0]