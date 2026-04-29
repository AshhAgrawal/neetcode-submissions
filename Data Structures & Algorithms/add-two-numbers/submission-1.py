# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify result list construction
        # WHY? → avoids handling head separately
        dummy = ListNode()
        curr = dummy

        carry = 0  # carry from previous addition

        # Continue while there are digits left OR carry remains
        # WHY? → handle different lengths + final carry (e.g., 999 + 1)
        while l1 or l2 or carry:

            # Get values, default to 0 if list is exhausted
            # WHY? → allows handling unequal length lists
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Compute sum of digits + carry
            val = v1 + v2 + carry

            # Update carry for next iteration
            # WHY //10? → extract carry digit
            carry = val // 10

            # Keep only the unit digit
            # WHY %10? → digit to store in current node
            val = val % 10

            # Create new node with computed digit
            curr.next = ListNode(val)

            # Move pointer forward
            curr = curr.next

            # Move input list pointers forward if possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return result list (skip dummy node)
        return dummy.next