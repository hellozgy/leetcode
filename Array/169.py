
# 参考答案
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count==0:
                count+=1
                m = nums[i]
            elif nums[i]!=m:
                count-=1
            else:
                count+=1
        return m
        
        