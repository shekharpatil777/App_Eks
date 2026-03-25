class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. Split the string into a list of words (handles extra spaces automatically)
        words = s.split()
        
        # 2. Reverse the list of words in-place
        words.reverse()
