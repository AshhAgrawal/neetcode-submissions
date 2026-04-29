# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify edge cases (like empty result list)
        # WHY? → avoids handling head separately
        dumm = ListNode()

        # Tail pointer to build the merged list
        tail = dumm

        # Pointers to traverse both lists
        l1 = list1
        l2 = list2

        # Traverse both lists until one becomes empty
        while l1 and l2:
            # Compare current nodes
            # WHY? → we need to maintain sorted order
            if l1.val < l2.val:
                tail.next = l1   # attach smaller node
                l1 = l1.next     # move pointer forward
            else:
                tail.next = l2
                l2 = l2.next

            # Move tail forward
            # WHY? → always point to last node in merged list
            tail = tail.next

        # Attach remaining nodes (only one list will have nodes left)
        # WHY? → remaining list is already sorted
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # Return merged list (skip dummy node)
        return dumm.next