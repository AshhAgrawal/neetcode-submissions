# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # This will store the maximum diameter found so far
        # WHY: Diameter can be at any node, not necessarily root
        self.diameter = 0

        def depth(node):
            # Base case: null node has depth 0
            # WHY: No nodes below this point
            if not node:
                return 0
            
            # Recursively get depth of left subtree
            leftDepth = depth(node.left)
            
            # Recursively get depth of right subtree
            rightDepth = depth(node.right)

            # Update diameter using current node
            # WHY: Longest path through this node = leftDepth + rightDepth
            self.diameter = max(self.diameter, leftDepth + rightDepth)

            # Return height of current node
            # WHY: Parent needs height to compute its own diameter
            return 1 + max(leftDepth, rightDepth)

        # Start DFS from root
        depth(root)
        
        # Return maximum diameter found
        return self.diameter