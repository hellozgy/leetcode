class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:return len(nums)
        
        cindex = -1
        next = 0
        while next<len(nums):
            if nums[next]==val:
                next +=1
            else:
                cindex+=1
                nums[cindex]=nums[next]
                next +=1
        return cindex+1
                