# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        
        new_head, new = None, None
        cnode = head
        pre = None
        while cnode:
            if cnode.next is None or cnode.val != cnode.next.val:
                if new is None:
                    new,new_head = cnode,cnode                   
                else:
                    new.next = cnode
                    new = new.next
                cnode = cnode.next
            else:
                while cnode.next and cnode.next.val==cnode.val:
                    cnode = cnode.next
                if cnode:cnode = cnode.next
        if new:
            new.next = None
        return new_head
                    
                    