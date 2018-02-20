class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return nums[0]
        small = [nums[0]]
        big = [nums[0]]
        for i in range(1, len(nums)):
            a = nums[i]*small[i-1]
            b = nums[i]*big[i-1]
            big.append(max(a, b, nums[i]))
            small.append(min(a, b, nums[i]))
            
        