class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If subRoot is empty, it is always a subtree
        # WHY: An empty tree is considered a subtree of any tree
        if not subRoot:
            return True

        # If main tree becomes empty but subRoot is still not found
        # WHY: No more nodes left to match → cannot be a subtree
        if not root:
            return False
        
        # Check if trees match starting from current node
        # WHY: A subtree must match exactly from some node in the main tree
        if self.sameTree(root, subRoot):
            return True

        # Otherwise, recursively check left and right subtree
        # WHY: The matching subtree could start at any node in the tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If both nodes are None → trees match at this branch
        # WHY: Reached end of both trees simultaneously → structure matches
        if not root and not subRoot:
            return True

        # If both nodes exist and values match → check children
        # WHY: Subtree match requires:
        # 1. Same value
        # 2. Left subtrees match
        # 3. Right subtrees match
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

        # If one is None or values differ → not a match
        # WHY: Structure or value mismatch breaks subtree condition
        return False