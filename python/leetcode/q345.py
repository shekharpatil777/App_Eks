class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
