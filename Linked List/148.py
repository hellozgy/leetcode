# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.qsort(head, None)
        
    def qsort(self, start, end):
        if start==None or start.next is None or start==end:return start
        index = start.next
        index1, index2 = start, start.next
        tag = start.val
        while index != end:
            if index.val<tag:
                index1.val = index.val
                index.val = index2.val
                index2.val = tag
                index1 = index1.next
                index2 = index2.next
            elif index.val==tag:
                index.val = index2.val
                index2.val = tag
                index2 = index2.next
            index = index.next
        res = self.qsort(start, index1)
        self.qsort(index2, end)
        return res

so = Solution()
node4 = ListNode(4)
node2 = ListNode(2)
node1 = ListNode(1)
node3 = ListNode(3)
node4.next = node2
node2.next = node1
node1.next = node3
res = so.sortList(node4)
print(res)