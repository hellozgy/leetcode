# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方案一：
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        res = []
        nodes = [root]
        _nodes = set()
        while len(nodes)>0:
            cnode = nodes[-1]
            if cnode.left is None or cnode.left in _nodes:
                res.append(cnode.val)
                _nodes.add(nodes.pop())
                if cnode.right is not None:
                    nodes.append(cnode.right)
            else:
                nodes.append(cnode.left)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
'''
 # 方案二：
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        nodes = []
        while root or nodes:
            while root:
                nodes.append(root)
                root = root.left
        
            if nodes:
                cnode = nodes.pop()
                res.append(cnode.val)
                root = cnode.right
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True 
            