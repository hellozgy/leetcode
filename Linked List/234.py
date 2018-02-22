# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:return True
        
        slow,fast = head, head
        pre = head
        next = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = next
            next = slow.next
            slow.next = pre
            if pre==head:
                pre.next = None
            pre = slow
            
        if fast is None:# 偶数个节点
            if slow.val!=slow.next.val:return False
            else:
                p1 = slow.next.next
                p2 = next
        # 奇数个节点
        elif fast.next is None:
            p1 = slow.next
            p2 = next

        while p1 and p2:
            if p1.val != p2.val:return False
            p1 = p1.next
            p2 = p2.next
        
        if p1 or p2:return False
        else:
            return True