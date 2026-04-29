# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        # Queue for BFS traversal
        # WHY queue? → BFS processes nodes level by level
        q = collections.deque()
        q.append(root)
        
        while q:
            # Number of nodes in current level
            # WHY store length? → ensures we process one level at a time
            qLen = len(q)

            level = []

            for i in range(qLen):
                node = q.popleft()

                # Check if node exists
                # WHY? → avoids processing None nodes
                if node:
                    # Add node value to current level
                    level.append(node.val)

                    # Add children to queue for next level
                    # WHY? → BFS explores next layer
                    q.append(node.left)
                    q.append(node.right)

            # Add level only if it has valid nodes
            # WHY? → prevents adding empty levels (from None nodes)
            if level:
                res.append(level)

        return res