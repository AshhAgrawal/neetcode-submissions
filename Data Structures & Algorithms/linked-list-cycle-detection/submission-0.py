# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        hashset = set()
        while curr:
            if not curr:
                return False
            if curr in hashset:
                return True
            hashset.add(curr)
            curr = curr.next
        return False
            