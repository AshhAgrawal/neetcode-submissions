# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # Queue for BFS (level-order traversal)
        # WHY? → we process tree level by level
        q = collections.deque()
        q.append(root)

        while q:
            # Number of nodes in current level
            qLen = len(q)

            level = []  # store values of current level

            for i in range(qLen):
                node = q.popleft()

                if node:
                    # Add node value
                    level.append(node.val)

                    # Add children for next level
                    q.append(node.left)
                    q.append(node.right)

            # Take the last element of this level
            # WHY? → rightmost node is visible from right side
            if level:
                res.append(level.pop())

        return res