# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers
        # curr → moves 1 step (slow pointer)
        # fast → moves 2 steps (fast pointer)
        curr = head
        fast = head

        # Traverse while fast pointer can move ahead
        # WHY fast and fast.next? → to avoid null pointer errors
        while fast and fast.next is not None:

            # Move slow pointer by 1 step
            curr = curr.next

            # Move fast pointer by 2 steps
            fast = fast.next.next

            # If they meet, cycle exists
            # WHY? → fast pointer laps slow pointer in a cycle
            if curr == fast:
                return True

        # If fast reaches end → no cycle
        return False