# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Store global maximum path sum
        # WHY list? → allows modification inside nested function (closure)
        res = [root.val]

        def dfs(root):
            # Base case: no node contributes 0
            if not root:
                return 0
            
            # Recursively get max path sum from left and right
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Ignore negative paths
            # WHY? → negative paths reduce total sum
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update global maximum
            # WHY include both left and right?
            # → this is the case where path passes through current node
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return max path contribution to parent
            # WHY only one side? → path must be continuous (no splits upward)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]