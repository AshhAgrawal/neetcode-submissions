# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node to handle edge cases (like removing head)
        # WHY? → avoids special handling when head needs to be removed
        dum = ListNode(0, head)

        # l → slow pointer, r → fast pointer
        l = dum
        r = head

        # Move fast pointer n steps ahead
        # WHY? → create a gap of n between l and r
        for n in range(n):
            r = r.next
        
        # Move both pointers until fast reaches end
        # WHY? → l will be just before the node to remove
        while r:
            l = l.next
            r = r.next

        # Remove the nth node from end
        # WHY? → l.next is the target node
        l.next = l.next.next

        # Return new head (skip dummy)
        return dum.next