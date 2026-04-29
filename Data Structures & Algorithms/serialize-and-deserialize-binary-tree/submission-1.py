# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []  # This will store the serialized values in preorder

        def dfs(root):
            # If node is None, we record it explicitly
            # WHY: Needed to reconstruct exact tree structure during deserialization
            if not root:
                res.append("N")
                return
            
            # Store current node value
            # WHY: Preorder = root first, so we process it before children
            res.append(str(root.val))
            
            # Traverse left subtree
            dfs(root.left)
            
            # Traverse right subtree
            dfs(root.right)
        
        # Start DFS traversal from root
        dfs(root)
        
        # Convert list to string using delimiter
        # WHY: Easy to split later during deserialization
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split string back into list of values
        # WHY: Reverse of serialize step
        vals = data.split(",")
        
        # Pointer to track current index in vals
        # WHY: We need shared state across recursive calls
        self.i = 0

        def dfs():
            # If current value is "N", this represents a null node
            if vals[self.i] == "N":
                self.i += 1  # Move pointer forward
                return None
            
            # Create node from current value
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # Move pointer to next value
            
            # Reconstruct left subtree
            # WHY: Must follow same preorder structure used in serialize
            node.left = dfs()
            
            # Reconstruct right subtree
            node.right = dfs()
            
            return node
        
        # Start reconstruction from root
        return dfs()