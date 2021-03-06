# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:return head
        head, next = head, head.next
        head.next = None
        tmp = self.reverseList(next)
        next.next = head
        return tmp