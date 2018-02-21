# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:return []
        res = []
        t=[]
        tt = [root]
        ttt = []
        while len(tt)>0:
            for node in tt:
                t.append(node.val)
                if node.left:ttt.append(node.left)
                if node.right :ttt.append(node.right)
            res.append(t)
            tt = ttt
            ttt = []
            t = []
        res.reverse()
        return res