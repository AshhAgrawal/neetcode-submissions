# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Step 1: Find middle of the list (slow/fast pointers)
        slow = head
        fast = head.next

        # WHY fast=head.next?
        # → helps split list into two halves correctly for even length
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half of the list
        second = slow.next

        # Break the list into two halves
        # WHY? → prevents cycles and allows independent processing
        prev = slow.next = None

        # Reverse the second half
        while second:
            temp = second.next  # store next node
            second.next = prev  # reverse pointer
            prev = second       # move prev forward
            second = temp       # move forward

        # Step 3: Merge two halves alternately
        first, second = head, prev

        # Merge nodes: first → second → first → second...
        while second:
            temp1, temp2 = first.next, second.next

            # Link first node to second node
            first.next = second

            # Link second node to next of first
            second.next = temp1

            # Move both pointers forward
            first, second = temp1, temp2