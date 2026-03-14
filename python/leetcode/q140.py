class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # O(1) lookups
        memo = {}

        def backtrack(remaining_s):
            # If we've already solved this suffix, return it
            if remaining_s in memo:
                return memo[remaining_s]
            
            # Base case: if the string is empty, return a list with an empty string
            if not remaining_s:
                return [""]

            res = []
            
            # Try every possible split point
            for i in range(1, len(remaining_s) + 1):
                prefix = remaining_s[:i]
                
                if prefix in word_set:
                    # Get all valid sentences for the rest of the string
                    suffixes = backtrack(remaining_s[i:])
                    
                    for suffix in suffixes:
                        # Join prefix and suffix with a space
                        sentence = (prefix + " " + suffix).strip()
                        res.append(sentence)
            
            memo[remaining_s] = res
            return res

        return backtrack(s)