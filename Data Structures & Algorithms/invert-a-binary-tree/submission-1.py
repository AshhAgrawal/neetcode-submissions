# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Store current node (not really needed, but shows intention of working on current node)
        cur = root
        
        # Base case: if node is None, nothing to invert
        # WHY: Recursion stops when we reach beyond leaf nodes
        if not root:
            return None
        
        # Swap left and right children
        # WHY: Inverting a tree means mirroring it → left becomes right, right becomes left
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursively invert left subtree (which was originally right)
        # WHY: After swapping, we still need to fix subtrees
        self.invertTree(root.left)
        
        # Recursively invert right subtree (which was originally left)
        self.invertTree(root.right)
        
        # Return the root of the inverted subtree
        return root