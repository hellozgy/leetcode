# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方案一：层次遍历 O(n)
'''
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        t = [root]
        tt = []
        depth = 0
        while len(t)>0:
            depth += 1
            for node in t:
                if node.left is not None:tt.append(node.left)
                if node.right is not None:tt.append(node.right)
            t = tt
            tt = []
        return depth
'''
# 方案二：递归 O(n)  
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        lheight = self.maxDepth(root.left)
        rheight = self.maxDepth(root.right)
        return max(lheight, rheight)+1
            