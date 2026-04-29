# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None → trees match at this branch
        # WHY: Reached end of both trees simultaneously
        if not p and not q:
            return True

        # If both nodes exist and values match → check subtrees
        # WHY:
        # 1. Current values must be equal
        # 2. Left subtrees must match
        # 3. Right subtrees must match
        if p and q and p.val == q.val:
            return (
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)
            )

        # If one node is None or values differ → not same tree
        # WHY: Structure or value mismatch
        else:
            return False