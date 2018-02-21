# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        t = [root]
        tt = []
        depth = 0
        while len(t)>0:
            depth+=1
            for node in t:
                if node.left:tt.append(node.left)
                if node.right:tt.append(node.right)
                if not node.left and not node.right:return depth
            t = tt
            tt = []
        
        