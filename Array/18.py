class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)==0:return []
        nums = sorted(nums)
        res = []
        pre = nums[0]+1
        for i in range(len(nums)-1):
            first = nums[i]
            if first == pre:continue
            pre = first
            _res = self.threeSum(nums, target-first, i+1, len(nums)-1)
            for t in _res:
                res.append([first]+t)
        return res
            
    def threeSum(self, nums, target, start, end):
        res = []
        pre = nums[start]+1
        for i in range(start, end+1):
            first = nums[i]
            if first == pre:continue
            pre = first
            _res = self.twoSum(nums, target-first, i+1, end)
            for t in _res:
                res.append([first]+t)
        return res
    
    def twoSum(self, nums, target, start, end):
        res = []
        while start < end:
            if nums[start]+nums[end] == target:
                res.append([nums[start], nums[end]])
                start += 1
                while start<end and nums[start]==nums[start-1]:
                    start+=1
            elif nums[start]+nums[end] > target:
                end -= 1
                while end>start and nums[end]==nums[end+1]:
                    end-=1
            else:
                start += 1
                while start<end and nums[start]==nums[start-1]:
                    start+=1
        return res
        
        
so = Solution()
res = so.fourSum([1, 0, -1, 0, -2, 2], 0)
print(res)