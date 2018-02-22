# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:return head
        n = 0
        p = head
        while p:
            n+=1
            p = p.next
        k = k%n
        if k==0:return head
        p1,p2 = None, None
        tag = 0
        while True:
            p1 = p1.next if p1 else head
            tag += 1
            if tag==k:break

        while p1.next:
            p1 = p1.next
            p2 = p2.next if p2 else head
        p1.next = head
        new = p2.next
        p2.next = None
        return new