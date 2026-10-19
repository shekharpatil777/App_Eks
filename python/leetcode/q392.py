class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        len_s, len_t = len(s), len(t)
