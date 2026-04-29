class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Hashmap to store mapping from original node → copied node
        # WHY: Helps us connect next and random pointers correctly
        # Also initialize None → None to handle edge cases easily
        copyhash = {None: None}

        curr = head

        # -------- Pass 1: Create copy of each node --------
        while curr:
            # Create a new node with same value
            copy = Node(curr.val)

            # Map original node to its copy
            copyhash[curr] = copy

            # Move to next node
            curr = curr.next

        curr = head

        # -------- Pass 2: Assign next and random pointers --------
        while curr:
            # Get copied node corresponding to current original node
            copy = copyhash[curr]

            # Set next pointer
            # WHY: copy.next should point to copy of curr.next
            copy.next = copyhash[curr.next]

            # Set random pointer
            # WHY: copy.random should point to copy of curr.random
            copy.random = copyhash[curr.random]

            # Move to next node
            curr = curr.next

        # Return head of copied list
        return copyhash[head]