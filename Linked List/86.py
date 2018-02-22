# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        l1 = []
        l2= []
        node = head
        while node:
            if node.val<x:
                l1.append(node)
            else:
                l2.append(node)
            node = node.next
        new = None
        new_head = None
        l1.extend(l2)
        for node in l1:
            if new is None:
                new = node
                new_head = new
            else:
                new.next = node
                new= node
        if new:new.next = None
        return new_head
        
            
        