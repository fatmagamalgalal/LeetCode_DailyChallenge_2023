// Author: Fatma Gamal Eldin Galal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        q = [root]
        res = []
        alt = 0
        # traverse BFS using queue
        while len(q) > 0:
            level = []
            lev_size = len(q)
            
            # loop over nodes of each level
            for i in range(lev_size):
                cur = q.pop(0)
                level.append(cur.val) # or insert reversely here
                # print(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            
            # reverse levels alternatingly 
            if alt%2==1:
                level.reverse()
            res.append(level)
            alt+=1
        return res
