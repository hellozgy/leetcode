# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1,p2=None,None
        for i in range(n):
            p1 = p1.next if p1 else head
        while p1.next:
            p2 = p2.next if p2 else head
            p1 = p1.next
        if p2 is None:return head.next
        else:
            p2.next = p2.next.next
            return head