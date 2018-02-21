# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#方案一：
'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None :return True
        return self.t(root.left, root.right)
        
    def t(self, p, q):
        if p==None and q==None :return True
        if p==None and q!=None :return False
        if p!= None and q==None :return False
        if p.val != q.val:return False
        return self.t(p.left, q.right) and self.t(p.right, q.left)
'''

#方案二
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """  
        if root is None:return True
        l1, l2 = [root.left],[root.right]
        while len(l1)>0 :
            lnode = l1.pop(0)
            rnode = l2.pop(0)
            if lnode is None and rnode is None:continue
            if (lnode is not None and rnode is None) or (lnode is None and rnode is not None):return False
            if lnode.val != rnode.val :return False
            l1.append(lnode.left)
            l1.append(lnode.right)
            l2.append(rnode.right)
            l2.append(rnode.left)
        return True