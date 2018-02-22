# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cnode = head
        pre = None
        new = None
        while cnode:
            if cnode.val!=val:
                if pre:
                    pre.next = cnode
                else:
                    new = cnode
                pre = cnode
            cnode = cnode.next
        if pre: pre.next = None
        return new