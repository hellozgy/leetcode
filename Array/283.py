# 不是最优的
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1<len(nums):
            while p1<len(nums) and nums[p1]!=0:
                p1 += 1
            for j in range(p1+1, len(nums)):
                if nums[j]!=0:
                    nums[p1]=nums[j]
                    nums[j]=0
                    break
            if p1<len(nums) and nums[p1]==0:break   
'''

# 参考答案
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for num in nums:
            if num!=0:
                nums[index]=num
                index+=1
        for i in range(index, len(nums)):
            nums[i]=0
               