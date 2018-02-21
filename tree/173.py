# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历
# 参考答案
# 方案一
'''
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [] 
        self.pushAll(root)
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.nodes)>0
        

    def next(self):
        """
        :rtype: int
        """
        cnode = self.nodes.pop()
        self.pushAll(cnode.right)
        return cnode.val
    
    def pushAll(self, node):
        while node:
            self.nodes.append(node)
            node = node.left
'''  

# 方案二：      
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [] if root is None else [root]
        self._nodes = set()
        self.cnode = None
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.nodes:
            cnode = self.nodes[-1]
            if cnode.left is None or cnode.left in self._nodes:
                self.cnode = self.nodes.pop()
                self._nodes.add(cnode)
                if cnode.right:
                    self.nodes.append(cnode.right)
                return  True
            else:
                self.nodes.append(cnode.left)
            
        return False
        
    def next(self):
        """
        :rtype: int
        """
        return self.cnode.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())