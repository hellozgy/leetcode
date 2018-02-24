class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:return len(nums)
        
        cindex = 0
        next = 1
        while next<len(nums):
            if nums[next]==nums[cindex]:
                next +=1
            else:
                cindex+=1
                nums[cindex]=nums[next]
                next +=1
        return cindex+1
                