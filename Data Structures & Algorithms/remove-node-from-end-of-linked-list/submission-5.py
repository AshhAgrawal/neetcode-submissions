# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0, head)
        l = dum
        r = head
        for n in range(n):
            r = r.next
        
        while r:
            l = l.next
            r = r.next
        # print(l.next.val )
        l.next = l.next.next
        return dum.next
    

