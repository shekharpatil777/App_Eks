def wordBreak(s: str, wordDict: list[str]) -> bool:
    # Convert list to set for O(1) lookups
    word_set = set(wordDict)
    # dp[i] means s[:i] can be segmented
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            # If the prefix s[:j] is valid AND s[j:i] is in the dict
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break # Move to the next i once we find a valid split
                
    return dp[len(s)]