# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n<1:return []
        subtree = [[None for _ in range(1+n)] for _ in range(1+n)]
        for i in range(1, 1+n):
            subtree[i][i] = [TreeNode(i)]
        for step in range(1, n):
            for i in range(1, n-step+1):
                subtree[i][i+step] = self.build(subtree, i, i+step)
        return subtree[1][n]
        
    def build(self, subtree, low, high):
        res = []
        for i in range(low, high+1):
            lchild = subtree[low][i-1] if i>low else [None]
            rchild = subtree[i+1][high] if high > i else [None]
            root = [TreeNode(i) for _ in range(len(lchild)*len(rchild))]
            for l in range(len(lchild)):
                for r in range(len(rchild)):
                    root[l*len(rchild)+r].left = lchild[l]
                    root[l*len(rchild)+r].right = rchild[r]
            res.extend(root)
        return res
            
so = Solution()
print(len(so.generateTrees(0)))
