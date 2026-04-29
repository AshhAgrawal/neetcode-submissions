# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Base case: if no elements, return None
        # WHY? → no tree to construct
        if not preorder or not inorder:
            return None

        # First element in preorder is always the root
        # WHY? → preorder = root → left → right
        root = TreeNode(preorder[0])

        # Find root index in inorder
        # WHY? → inorder = left → root → right
        # This splits tree into left and right subtrees
        mid = inorder.index(preorder[0])

        # Build left subtree
        # preorder[1:mid+1] → elements after root belonging to left subtree
        # inorder[:mid] → left subtree elements
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Build right subtree
        # preorder[mid+1:] → remaining elements
        # inorder[mid+1:] → right subtree elements
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root