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
# 方案2
'''
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:return []
        tag = [[None for _ in range(n+1)] for _ in range(n+1)]
        return self.build(1, n, tag)
    def build(self, low, high, tag):
        if high<low:return [None]
        if low==high:return [TreeNode(low)]
        if tag[low][high]:return tag[low][high]
        res = []
        for i in range(low, high+1):
            left = self.build(low, i-1, tag)
            right = self.build(i+1, high, tag)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        tag[low][high]=res
        return res

'''
so = Solution()
print(len(so.generateTrees(0)))
