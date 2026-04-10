class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            # ord(char) gets the ASCII value
            # ord('A') is 65, so subtracting 64 gives A=1, B=2, etc.
            value = ord(char) - ord('A') + 1
