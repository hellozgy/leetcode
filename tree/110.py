# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方案一：O(n^2)
'''
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:return True
        if abs(self.depth(root.left)-self.depth(root.right))>1:return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def depth(self, root):
        if root is None:return 0
        depth = 0
        t = [root]
        tt = []
        while len(t)>0:
            depth += 1
            for node in t:
                if node.left:tt.append(node.left)
                if node.right: tt.append(node.right)
            t = tt
            tt = []
        return depth
'''
#方案二 ：O(n) 
#借鉴题目的解析

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root)!=-1
        
    def dfsHeight(self, node):
        '''
            如果节点node是不平衡的，则返回-1，否则返回它的实际深度
        '''
        if node is None:return 0
        
        lheight = self.dfsHeight(node.left)
        if lheight==-1:return -1 # 如果子节点不平衡，那么父节点也不平衡
        rheight = self.dfsHeight(node.right)
        if rheight==-1:return -1
        
        if abs(lheight-rheight)>1:return -1
        
        return max(lheight, rheight)+1    