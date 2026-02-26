from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Layer-based BFS to build the graph
        layer = {beginWord}
        parents = defaultdict(set)
        
        while layer and endWord not in parents:
            next_layer = defaultdict(set)
            for word in layer:
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in wordSet and new_word not in parents:
                            next_layer[new_word].add(word)
            
            # Update parents with the paths found in this layer
            for word, p_set in next_layer.items():
                parents[word].update(p_set)
            
            # Move to the next level
            layer = set(next_layer.keys())
            # Remove words we've already "visited" so we don't go backwards
            wordSet -= set(next_layer.keys())

