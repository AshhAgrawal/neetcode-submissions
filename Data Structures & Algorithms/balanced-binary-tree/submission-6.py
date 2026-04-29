# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(isBalanced, node):
            if not node:
                return [True, 0]
            left = dfs(isBalanced, node.left)
            right = dfs(isBalanced, node.right)
            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [isBalanced, 1 + max(left[1], right[1])]
        return dfs(True, root)[0]