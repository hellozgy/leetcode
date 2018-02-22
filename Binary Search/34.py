class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index, _start, _end = self.find(nums, 0, len(nums)-1, target)
        if index == -1:return [-1, -1]
        else:
            start = self.lfind(nums, _start, index, target)
            end = self.rfind(nums, index, _end, target)
            return [start, end]
            
    def find(self, nums, start, end, target):
        while start <= end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid, start, end
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return -1, -1, -1
        
    def lfind(self, nums, start, end, target):
        while start<end:
            mid = (start+end)//2
            if nums[mid]==target:end = mid
            else:start = mid+1
        return start
        
    def rfind(self, nums, start, end, target):
        while start<end:
            mid = (start+end)//2+1
            if nums[mid]==target:start = mid
            else:end = mid-1
        return end 
so = Solution()
print(so.searchRange([5, 7, 7, 8, 8, 10], 8))
           