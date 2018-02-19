class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)):
            if i == 0:res.append(nums[0])
            else:
                res.append(max(nums[i], nums[i]+res[i-1]))
        return max(res)


