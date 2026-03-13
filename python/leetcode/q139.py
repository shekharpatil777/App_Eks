def wordBreak(s: str, wordDict: list[str]) -> bool:
    # Convert list to set for O(1) lookups
    word_set = set(wordDict)
    # dp[i] means s[:i] can be segmented
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
