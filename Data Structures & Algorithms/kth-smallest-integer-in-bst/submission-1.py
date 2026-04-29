# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack for iterative inorder traversal
        # WHY stack? → simulate recursion (DFS)
        stack = []

        cur = root

        # Continue while there are nodes to process
        while cur or stack:

            # Go as left as possible
            # WHY? → inorder = left → node → right
            # Leftmost node is the smallest
            while cur:
                stack.append(cur)
                cur = cur.left

            # Process node
            cur = stack.pop()

            # Decrement k
            # WHY? → we are visiting nodes in sorted order
            k -= 1

            # If this is the kth node → return value
            if k == 0:
                return cur.val

            # Move to right subtree
            # WHY? → next larger elements are in right subtree
            cur = cur.right