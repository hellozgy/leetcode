# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:return head
        helper = ListNode(float('-inf'))
        cur = helper
        tmp = head
        while tmp:
            next = tmp.next
            while cur.next and cur.next.val<tmp.val:
                cur = cur.next
            cnext = cur.next
            cur.next = tmp
            tmp.next = cnext
            tmp = next
            cur = helper
        return helper.next