class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        comb = []
        candidates = sorted(candidates)
        self.f(candidates, target, res, comb)
        return res
    
    def f(self, nums, target, res, comb):
        if target==0:
            res.append(comb)
            return 
        if len(nums)==0 or target<0:return 

        
        self.f(nums[1:], target-nums[0], res, comb+[nums[0]])
        index = 1
        while index<len(nums) and nums[index]==nums[0]:index+=1
        self.f(nums[index:], target, res, comb)
            
        
so = Solution()
print(so.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))       