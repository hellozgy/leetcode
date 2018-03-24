class TreeNode:
    def __init__(self, val, left= None, right=None):
        self.left = left
        self.right = right
        self.val = val
class Solution:
    def postorder(self, root):
        pre = None
        stack = [root]
        if root==None:return
        while stack:
            cur = stack[-1]
            if (cur.left is None and cur.right is None) or (pre is not None and (pre==cur.left or pre==cur.right)):
                stack.pop()
                print(cur.val)
                pre = cur
            else:
                if cur.right:stack.append(cur.right)
                if cur.left:stack.append(cur.left)
        
        
        

node6 = TreeNode(6)
node4 = TreeNode(4, left=node6)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5) 
node9 = TreeNode(9)
node8 = TreeNode(8, right= node9)
node3 = TreeNode(3, left = TreeNode(7), right=node8)
node1 = TreeNode(1, node2, node3)
so = Solution()
so.postorder(node1)