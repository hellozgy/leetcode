class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        comb = []
        self.f(candidates, target, res, comb)
        return res
    
    def f(self, nums, target, res, comb):
        if target==0:
            res.append(comb)
            return 
        if len(nums)==0 or target<0:return 
        n = target//nums[0]
        for i in range(n+1):
            if target-nums[0]*i>=0:
                self.f(nums[1:], target-nums[0]*i, res, comb+[nums[0] for _ in range(i)])
            
        
so = Solution()
print(so.combinationSum([2, 3, 6, 7], 7))       