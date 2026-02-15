class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] = number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty t
        
