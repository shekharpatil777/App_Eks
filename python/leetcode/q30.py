class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}

        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        res = []

        for i in range(word_len):  # offset sliding window
            left = i
            right = i
            current_count = {}
            count = 0

            while right + word_len <= len(s):
                w = s[right:right + word_len]
                right += word_len

                if w in word_count:
                    current_count[w] = current_count.get(w, 0) + 1
                    count += 1



        return res
