class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] will store the number of ways to decode s[:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1 # An empty string has 1 way to be decoded (doing nothing)
        dp[1] = 1 # We already checked that s[0] != '0'
        
