class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        n = len(words)
        
        for i in range(n):
            for j in range(len(words[i])):
                # 1. Column index j exceeds total rows available
                # 2. Row index i exceeds the length of words[j]
