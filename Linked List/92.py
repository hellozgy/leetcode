# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m==n:return head
        lnode = None
        
        cnode = head
        index = 0
        while cnode:
            index += 1
            if index == m:
                pre = cnode
                tail = cnode
                next = cnode.next
                for i in range(n-m):
                    cnode = next
                    next = cnode.next
                    cnode.next = pre
                    pre = cnode
                tail.next = next
                if lnode:
                    lnode.next = cnode
                    return head
                else:
                    return cnode
                
            lnode = cnode
            cnode = cnode.next