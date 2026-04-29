# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # Base case: empty tree is balanced with height 0
            if not node:
                return [True, 0]

            # Recursively get left subtree info
            leftHeight = dfs(node.left)

            # Recursively get right subtree info
            rightHeight = dfs(node.right)

            # Check if current node is balanced
            # WHY?
            # 1. Left subtree must be balanced
            # 2. Right subtree must be balanced
            # 3. Height difference ≤ 1
            balanced = (
                leftHeight[0] and
                rightHeight[0] and
                abs(leftHeight[1] - rightHeight[1]) <= 1
            )

            # Return:
            # [isBalanced, height]
            # WHY height? → needed by parent to check balance
            return [balanced, 1 + max(leftHeight[1], rightHeight[1])]

        # Return only the balance status
        return dfs(root)[0]