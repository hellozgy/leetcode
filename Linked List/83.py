# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return head
        
        node = head
        cnode = head.next
        while cnode:
            if node.val != cnode.val:
                node.next = cnode
                node = cnode
            cnode = cnode.next
        node.next = None
        return head