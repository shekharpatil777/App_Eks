class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j] = edit distance between word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i  # delete all characters
        for j in range(n + 1):
            dp[0][j] = j  # insert all characters


