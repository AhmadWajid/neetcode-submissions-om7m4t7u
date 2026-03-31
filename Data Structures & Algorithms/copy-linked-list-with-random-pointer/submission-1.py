"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        c_hash = {}
        curr = head
        while curr:
            c_hash[curr]= Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            c_hash[curr].next = c_hash.get(curr.next)
            c_hash[curr].random = c_hash.get(curr.random)
            curr = curr.next
        return c_hash[head]