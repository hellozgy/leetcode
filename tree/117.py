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
        if root is not None and (root.left or root.right):
            t =[root]
            tt = []
            while len(t)>0:
                for i in range(len(t)):
                    if i <len(t)-1:
                        t[i].next = t[i+1]
                    if t[i].left:tt.append(t[i].left)
                    if t[i].right:tt.append(t[i].right)
                t = tt
                tt = []
            
            