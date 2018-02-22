class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)//2
            if nums[mid]>nums[end]:
                start = mid+1
            else:
                end = mid
        rot = start
        return nums[rot]
