# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        new = None
        head = None
        while l1 and l2:
            if l1.val<=l2.val:
                if new:
                    new.next = l1
                    new = l1
                else:
                    new = l1
                    head = new
                l1 = l1.next
            else:
                if new:
                    new.next = l2
                    new = l2
                else:
                    new = l2
                    head = new
                l2 = l2.next
        if new is None:return l1 if l1 else l2
        if l1:new.next = l1
        elif l2:new.next = l2
        return head