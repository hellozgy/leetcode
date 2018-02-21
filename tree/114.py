# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """  
        if root is not None and (root.left or root.right):
            rchild = root.right
            lchild = root.left
            self.flatten(rchild)
            self.flatten(lchild)
            root.left = None
            root.right = lchild
            node = root 
            while node.right is not None:
                node = node.right
            node.right = rchild
        
        