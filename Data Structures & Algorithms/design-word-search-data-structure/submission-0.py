class TrieNode:
    def __init__(self):
        self.children = {}     # Letter -> next TrieNode
        self.is_end = False    # True if a word ends here


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            # Create node if letter doesn't exist
            if char not in curr.children:
                curr.children[char] = TrieNode()

            # Move to the next node
            curr = curr.children[char]

        # Mark the end of the word
        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            # Reached the end of the search word
            if i == len(word):
                return node.is_end

            char = word[i]

            if char == ".":
                # Dot can match ANY child node
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            else:
                # Normal letter must exist in children
                if char not in node.children:
                    return False

                return dfs(i + 1, node.children[char])

        return dfs(0, self.root)