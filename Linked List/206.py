# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next :return head
        
        prenode = None
        node = head
        while node:      
            next = node.next
            if prenode:
                node.next = prenode
                prenode = node
            else:
                prenode = node
                head.next = None            
            node = next
        return prenode
'''
# 递归
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        next = head.next
        head.next = None
        tnode = self.reverseList(next)
        next.next = head
        return tnode