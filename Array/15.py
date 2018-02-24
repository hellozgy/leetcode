# 借鉴参考答案

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        pre = None
        for i in range(len(nums)):
            if pre!=None and nums[i]==pre:continue
            else:pre = nums[i]
                
            start = i+1
            end = len(nums)-1
            while start<end:
                if nums[start]+nums[end]==-nums[i]:
                    res.append([nums[i], nums[start], nums[end]])
                    a = nums[start]
                    while nums[start]==a and start<end:start+=1
                elif nums[start]+nums[end]<-nums[i]:
                    start += 1
                else:
                    end -= 1
        return res
so = Solution()
print(so.threeSum([-1, 0, 1, 2, -1, -4]))