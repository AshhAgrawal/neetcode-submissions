# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node to simplify edge cases
        # WHY? → handles head changes cleanly
        dummy = ListNode(0, head)

        # Pointer to the node before current group
        groupPrev = dummy

        while True:
            # Find the kth node from groupPrev
            # WHY? → determines if a full group exists to reverse
            kth = self.getKth(groupPrev, k)

            # If fewer than k nodes remain → stop
            if not kth:
                break

            # Node after the kth node (start of next group)
            groupNext = kth.next

            # Reverse current group
            # prev starts at groupNext (important trick)
            # WHY? → ensures last node of reversed group connects correctly
            prev, curr = kth.next, groupPrev.next

            # Reverse nodes in current group
            while curr != groupNext:
                temp = curr.next      # store next node
                curr.next = prev      # reverse pointer
                prev = curr           # move prev forward
                curr = temp           # move curr forward
            
            # After reversal:
            # groupPrev.next is now the tail of this group
            tmp = groupPrev.next

            # Connect previous part to new head (kth node)
            groupPrev.next = kth

            # Move groupPrev to end of reversed group
            # WHY? → prepare for next group
            groupPrev = tmp

        return dummy.next


    def getKth(self, curr, k):
        # Move k steps ahead to find kth node
        # WHY? → ensures we only reverse full groups
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr