class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:return mid
            if nums[mid]>target:end = mid - 1
            else:
                start = mid+1
        return start       
            
        
        
so = Solution()
res = so.searchInsert([1, 3, 5, 6], 2)
print(res)