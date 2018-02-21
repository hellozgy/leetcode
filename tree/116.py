# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is not None and root.left is not None:
            root.left.next = root.right
            lchild = root.left
            rchild = root.right
            while lchild.right:
                lchild.right.next = rchild.left
                lchild = lchild.right
                rchild = rchild.left
            self.connect(root.left)
            self.connect(root.right)
                
            
            
            
            