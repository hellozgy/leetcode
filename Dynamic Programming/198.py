class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return 0
        if len(nums)<=2:return max(nums)
        res = []
        res.append(nums[0])
        res.append(max(nums[:2]))
        for i in range(2, len(nums)):
            res.append(max(res[i-1], res[i-2]+nums[i]))
        return res[-1]
        