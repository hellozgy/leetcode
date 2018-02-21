# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        nodes = [root]
        _nodes = [root]
        res = []
        while len(nodes)>0:
            cnode = nodes[-1]
            if cnode.left is None:
                if cnode.right is None:
                    res.append(int(''.join([str(node.val) for node in nodes])))
                    nodes.pop()
                elif cnode.right in _nodes:
                    nodes.pop()
                else:
                    nodes.append(cnode.right)
                    _nodes.append(cnode.right)
            elif cnode.left in _nodes:
                if cnode.right is None or cnode.right in _nodes:
                    nodes.pop()
                else:
                    nodes.append(cnode.right)
                    _nodes.append(cnode.right)
            else :
                nodes.append(cnode.left)
                _nodes.append(cnode.left)
        return sum(res)
            
        