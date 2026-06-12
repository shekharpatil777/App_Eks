from collections import defaultdict
from typing import List

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_map = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.word_map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.word_map[word1]
        list2 = self.word_map[word2]

        i = j = 0
        ans = float('inf')
