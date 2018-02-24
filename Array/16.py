class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = sum(nums[:3])
        nums = sorted(nums)
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            while start<end:
                s = nums[start]+nums[end]+nums[i]
                if s==target:
                    return target
                elif s<target:
                    start += 1
                    if abs(s-target)<abs(res-target):res = s
                else:
                    end -= 1
                    if abs(s-target)<abs(res-target):res = s
        return res
so = Solution()
print(so.threeSumClosest([1,1,1,0],-100))
            