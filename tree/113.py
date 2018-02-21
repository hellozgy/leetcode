# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:return []
        nodes = [root]
        _nodes = [root]
        m = root.val
        res = []
        while len(nodes)>0:
            cnode = nodes[-1]
            if cnode.left is None:
                if cnode.right is None:
                    if m==sum:
                        res.append([nn.val for nn in nodes])                    
                    m -= nodes.pop().val
                elif cnode.right in _nodes:
                    m -= nodes.pop().val
                else:
                    nodes.append(cnode.right)
                    m += cnode.right.val
                    _nodes.append(cnode.right)
                   
            elif cnode.left in _nodes:
                if cnode.right is None or cnode.right in _nodes:
                    m -= nodes.pop().val
                else:
                    nodes.append(cnode.right)
                    m += cnode.right.val
                    _nodes.append(cnode.right)
                   
            else:
                nodes.append(cnode.left)
                m += cnode.left.val
                _nodes.append(cnode.left)
        return res
                    
                    