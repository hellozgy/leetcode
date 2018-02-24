class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        self.f(nums, res, [])
        return res
    
    def f(self, nums, res, comb):
        if len(nums)==0:
            res.append(comb)
            return
        self.f(nums[1:], res, comb+[nums[0]])
        index = 1
        while index<len(nums) and nums[index]==nums[0]:index+=1
        self.f(nums[index:], res, comb)
so = Solution()
print(so.subsetsWithDup([1,2,2]))