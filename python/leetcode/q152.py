class Solution:
    def reverseWords(self, s: str) -> str:
        # .split() without arguments handles any amount of whitespace
        words = s.split()
        
        # Reverse the list of words in-place
        words.reverse()
        
        # Join them back with a single space
        return " ".join(words)