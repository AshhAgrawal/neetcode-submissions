class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # If input list is empty, nothing to merge
        # WHY: Edge case
        if not lists or len(lists) == 0:
            return None

        # Keep merging until only one list remains
        # WHY: We reduce k lists → k/2 → k/4 ... → 1 (divide & conquer)
        while len(lists) > 1:
            mergedLists = []

            # Merge lists in pairs
            # WHY: Pairwise merging reduces number of lists efficiently
            for i in range(0, len(lists), 2):
                
                l1 = lists[i]

                # Get next list if exists, otherwise None
                # WHY: Handle odd number of lists
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge two sorted lists and store result
                mergedLists.append(self.mergeLists(l1, l2))

            # Update lists with merged results
            # WHY: Next iteration works on smaller number of lists
            lists = mergedLists

        # Final merged list
        return lists[0]

    def mergeLists(self, l1, l2):
        
        # Dummy node to simplify list construction
        # WHY: Avoid handling head separately
        dummy = ListNode()
        tail = dummy

        # Merge two sorted linked lists
        while l1 and l2:

            # Pick smaller node and attach to result
            # WHY: Maintain sorted order
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            # Move tail forward
            # WHY: Always point to last node of merged list
            tail = tail.next
        
        # Attach remaining nodes (only one list will be non-empty)
        # WHY: No need to compare anymore
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        # Return merged list (skip dummy)
        return dummy.next