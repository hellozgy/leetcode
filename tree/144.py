# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:return []
        nodes = [root]
        _nodes = [root]
        res = [root.val]
        while len(nodes)>0:
            cnode = nodes[-1]
            if cnode.left is None or cnode.left in _nodes:
                if cnode.right is None or cnode.right in _nodes:
                    nodes.pop()
                else:
                    nodes.append(cnode.right)
                    _nodes.append(cnode.right)
                    res.append(cnode.right.val)
            else :
                nodes.append(cnode.left)
                _nodes.append(cnode.left)
                res.append(cnode.left.val)
        return res