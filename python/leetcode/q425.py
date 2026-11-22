from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []
        
        n = len(words[0])
        prefix_map = defaultdict(list)
        
        # Precompute all prefixes for quick candidate retrieval
        for word in words:
            for i in range(n):
                prefix_map[word[:i]].append(word)
        
        results = []
        
        def backtrack(step: int, current_square: List[str]):
            if step == n:
                results.append(list(current_square))
                return
            
            # Form the prefix required for the current row
            # It consists of the `step`-th character of each word placed so far
            prefix = "".join(word[step] for word in current_square)
            
            # Explore all matching candidate words
            for candidate in prefix_map.get(prefix, []):
                current_square.append(candidate)
                backtrack(step + 1, current_square)
                current_square.pop()
        
        # Start backtracking from every word as the first row
        for word in words:
            backtrack(1, [word])
            
        return results