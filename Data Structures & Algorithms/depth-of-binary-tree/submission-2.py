# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Initialize queue for BFS
        # WHY: We use level-order traversal to count depth level by level
        q = deque()
        
        # If root exists, add it to queue
        # WHY: BFS always starts from the root node
        if root:
            q.append(root)
        
        length = 0  # This will track number of levels (i.e., depth)

        # Continue until all levels are processed
        while q:
            
            # Process all nodes in current level
            # WHY: len(q) gives number of nodes at current depth level
            for i in range(len(q)):
                node = q.popleft()  # Remove node from front of queue
                
                # Add left child to queue
                # WHY: It will be part of next level
                if node.left:
                    q.append(node.left)
                
                # Add right child to queue
                if node.right:
                    q.append(node.right)
            
            # After processing one full level, increment depth
            length += 1
        
        # Final depth (number of levels)
        return length



