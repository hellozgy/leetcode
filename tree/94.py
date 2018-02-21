# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
# 中序遍历
# 方案一
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
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
        return res
'''
#方案二：
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        res = []
        while root or len(nodes)>0:
            while root:
                nodes.append(root)
                root = root.left
                
            if len(nodes)>0:
                cnode = nodes.pop()
                res.append(cnode.val)
                root = cnode.right
        return res