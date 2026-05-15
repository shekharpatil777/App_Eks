class TrieNode:
    def __init__(self):
        # Each node contains a dictionary of children and a boolean flag
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        current = self.root
        for char in word:
            # If the character isn't a child of the current node, add it
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the child node
            current = current.children[char]
        # Mark the end of the word
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        # Return True only if it's a complete word, not just a prefix
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = 