class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []

        for word in words:
            mask = 0

            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            masks.append(mask)

        ans = 0
