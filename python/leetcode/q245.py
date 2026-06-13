class Solution:
    def shortestWordDistance(self, wordsDict, word1, word2):
        ans = float('inf')

        if word1 == word2:
            prev = -1

            for i, word in enumerate(wordsDict):
                if word == word1:
                    if prev != -1:
                        ans = min(ans, i - prev)
                    prev = i
        else:
            idx1 = idx2 = -1

            for i, word in enumerate(wordsDict):
                if word == word1:
                    idx1 = i
                elif word == word2:
                    idx2 = i
