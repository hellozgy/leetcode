class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return 0
        return self.f(nums, 0, len(nums)-1, target)
    
    def f(self, nums, start, end, target):
        if start==end:
            if nums[start]==target:return start
            elif nums[start]<target:return start+1
            else: return start
        mid = (start+end)//2
        if nums[mid]==target:return mid
        elif nums[mid]>target:
            return start if mid==start else self.f(nums, start, mid-1, target)
        else:
            return mid+1 if mid==end else self.f(nums, mid+1, end, target)
so = Solution()
print(so.searchInsert([1,3,5,6], 5))
        