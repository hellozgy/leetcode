# Definition for a binary tree node.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """   
        if len(preorder)==0:return None
        if len(preorder)==1:return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        linorder = inorder[:root_index]
        rinorder = inorder[root_index+1:]  
       
        root.left = self.buildTree(preorder[1:1+len(linorder)], linorder) #所有的左子树比右子树节点先遍历，所以根据左子树节点数找到在前序中的下标范围
        root.right = self.buildTree(preorder[1+len(linorder):], rinorder)
        return root

so = Solution()
print(so.buildTree([3,9,20,15,7],[9,3,15,20,7]))