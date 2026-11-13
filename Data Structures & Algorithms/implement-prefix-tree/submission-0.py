class TrieNode:
    def __init__(self):
        self.children = {}       # Character -> next TrieNode
        self.is_end = False      # True if a complete word ends here


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()   # Starting node of the Trie

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            # Create a new node if character doesn't exist
            if char not in curr.children:
                curr.children[char] = TrieNode()

            # Move to the next character's node
            curr = curr.children[char]

        # Mark the end of a complete word
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            # If character doesn't exist, word isn't stored
            if char not in curr.children:
                return False

            curr = curr.children[char]

        # Must be a complete word, not just a prefix
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            # Prefix doesn't exist
            if char not in curr.children:
                return False

            curr = curr.children[char]

        # All prefix characters were found
        return True