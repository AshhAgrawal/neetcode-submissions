# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # DFS helper function
        # maxVal → maximum value seen from root to current node
        def dfs(node, maxVal):

            # Base case: no node
            if not node:
                return 0

            # Check if current node is "good"
            # WHY? → node is good if it's ≥ all previous values in path
            res = 1 if node.val >= maxVal else 0

            # Update max value for children
            # WHY? → pass updated path maximum down the tree
            maxVal = max(node.val, maxVal)

            # Recurse left and right and add results
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        # Start DFS with root value as initial max
        return dfs(root, root.val)