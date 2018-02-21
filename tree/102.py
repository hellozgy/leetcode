# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:return []
        t = [root]
        tt = []
        res = []
        vals = []
        while len(t)>0:
            for node in t:
                vals.append(node.val)
                if node.left:tt.append(node.left)
                if node.right:tt.append(node.right)
            res.append(vals)
            vals = []
            t = tt
            tt = []
        return res
            
            
            
            
            
    