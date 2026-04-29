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
            leftH = dfs(isBalanced, node.left)
            rightH = dfs(isBalanced, node.right)
            isBalanced = (leftH[0] and rightH[0] and
             (abs(leftH[1]  - rightH[1])) <= 1) 
            # print("hello")
            return [isBalanced,  1 + max(leftH[1], rightH[1])]
        
        return True if dfs(True, root)[0] else False