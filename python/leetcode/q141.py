class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)  # O(1) lookups
        memo = {}

        def dfs(remaining):
            # Return cached result if we've seen this suffix before
            if remaining in memo:
                return memo[remaining]
            
            # Base case: we reached the end of the string
            if not remaining:
                return [""]
            
            res = []
            # Try every possible split point
            for i in range(1, len(remaining) + 1):
                prefix = remaining[:i]
                
                if prefix in wordSet:
                    # Get all valid sentences for the rest of the string
                    suffixes = dfs(remaining[i:])
                    for suffix in suffixes:
                        # Join prefix and suffix with a space (if suffix isn't empty)
                        sentence = prefix + (" " + suffix if suffix else "")
                        res.append(sentence)
            

            memo[remaining] = res
            return res

        return dfs(s)