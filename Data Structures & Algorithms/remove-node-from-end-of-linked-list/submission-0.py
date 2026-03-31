# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        start = dummy
        dummy.next = head
        forward = dummy
        for i in range(n):
            forward = forward.next
        while forward.next:
            forward = forward.next
            start = start.next
        start.next = start.next.next
        return dummy.next
