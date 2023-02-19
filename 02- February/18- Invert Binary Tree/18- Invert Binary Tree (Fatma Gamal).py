// Author: Fatma Gamal Eldin Galal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def DFS(r): # inorder
            if r is None:
                return
            DFS(r.left)
            DFS(r.right)
            # swap each 2 children of a root node
            r.left, r.right = r.right, r.left
        
        DFS(root)
        return root
