class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        left = 0
        freq = {}
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
