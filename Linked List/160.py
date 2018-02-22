# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:return None
        pa = headA
        pb = headB
        a,b = 1,1
        while pa.next:
            a+=1
            pa = pa.next
        while pb.next:
            b += 1
            pb = pb.next
        if pa==pb:
            pa, pb = headA, headB
            if a>=b:
                for i in range(a-b):
                    pa = pa.next
            else:
                for i in range(b-a):
                    pb = pb.next
            while pa!=pb:
                pa = pa.next
                pb = pb.next
            return pa
            
        else:
            return None
            
        