class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        # Join words with spaces and include a trailing space
        s = " ".join(sentence) + " "
        n = len(s)
        start = 0
