class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {ch: i for i, ch in enumerate(s)}
        
        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue
