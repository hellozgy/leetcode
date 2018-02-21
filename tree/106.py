# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:return None
        
        root_index = inorder.index(postorder[-1])
        linorder = inorder[:root_index]
        rinorder = inorder[root_index+1:]
        
        root = TreeNode(postorder[-1])
        root.left = self.buildTree(linorder, postorder[:len(linorder)])
        root.right = self.buildTree(rinorder, postorder[len(linorder):-1])
        return root