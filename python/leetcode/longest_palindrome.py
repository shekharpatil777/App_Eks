class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in s using the expand around center method.
        """
        # Handle edge cases for empty or single-character strings
        if len(s) < 1 or s is None:
            return ""

        # These variables will store the start index and length of the longest palindrome found
        start = 0
        max_len = 1

        for i in range(len(s)):
            # --- Case 1: Odd length palindrome (center is at i) ---
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the current palindrome is longer than the max found so far, update
                if (r - l + 1) > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

            # --- Case 2: Even length palindrome (center is between i and i+1) ---
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the current palindrome is longer than the max found so far, update
                if (r - l + 1) > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
        
        return s[start : start + max_len]

