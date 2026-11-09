class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        # Join words with spaces and include a trailing space
        s = " ".join(sentence) + " "
        n = len(s)
        start = 0

        for _ in range(rows):
            start += cols
            # If the current character is a space, advance past it
            if s[start % n] == " ":
                start += 1
            else:
                # If cut in the middle of a word, retreat to the start of that word
                while start > 0 and s[(start - 1) % n] != " ":
                    start -= 1

        return start // n