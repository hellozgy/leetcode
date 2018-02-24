class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tt=0
        for i in range(len(nums)-1):
            tt = max(tt-1, nums[i])
            if tt==0:
                return False
            
        return True