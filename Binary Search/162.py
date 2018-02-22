
# 参考答案
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start<end:    
            mid = (start+end)//2
            mid2 = mid+1
            if nums[mid]<nums[mid2]:
                start = mid2
            else:
                end = mid
        return start