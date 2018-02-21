# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:return []
        t = [root]
        tt = []
        res = []
        while len(t)>0:
            res.append(t[-1].val)
            for node in t:
                if node.left:tt.append(node.left)
                if node.right:tt.append(node.right)
            t = tt
            tt = []
        return res