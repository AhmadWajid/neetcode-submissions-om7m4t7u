"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        copied = {}

        def copier(node):
            if node in copied:
                return copied[node]
            deep_copy = Node(node.val)
            copied[node] = deep_copy
            for nei in node.neighbors:
                    deep_copy.neighbors.append(copier(nei))
            return deep_copy
        return copier(node)