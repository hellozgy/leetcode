class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1, -1, -1):
            nums1[n+i]=nums1[i]
        p1,p2=0,0
        index = 0
        while p1<m and p2<n:
            a = nums1[n+p1]
            b = nums2[p2]
            if a<=b:
                nums1[index]=a
                index += 1
                p1 += 1
            else:
                nums1[index]=b
                index += 1
                p2 += 1
        if p1<m:
            while p1<m:
                nums1[index]=nums1[n+p1]
                p1+=1
                index+=1
        elif p2<n:
            while p2<n:
                nums1[index]=nums2[p2]
                p2+=1
                index+=1
l1=[1,2,3,4,0,0]
l2=[2]
so=Solution()
so.merge(l1,4,l2,1)
print(l1)