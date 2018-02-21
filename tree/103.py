# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:return []
        t = [root]
        tt = []
        res = []
        val = []
        while len(t)>0:
            for node in t:
                val.append(node.val)
                if node.left:tt.append(node.left)
                if node.right:tt.append(node.right)
            t = tt
            tt = []
            res.append(val)
            val = []
        for i in range(1, len(res), 2):
            res[i].reverse()
        return res