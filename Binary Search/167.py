# 我的答案
'''
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = set(numbers)
        for i in range(len(numbers)):
            a = numbers[i]
            b = target - a
            if b in nums and (a != b or numbers[i+1]==a):
                return [i+1, self.f(numbers, i+1, len(numbers)-1, b)]
    
    def f(self, nums, start, end, target):
        if start==end:return start+1
        mid = (start+end)//2
        if nums[mid]==target:return mid+1
        elif nums[mid]<target:return self.f(nums, mid+1, end, target)
        else:return self.f(nums, start, mid-1, target)
so = Solution()
print(so.twoSum([0, 0, 2,3,4], 0))
'''
# 参考答案

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while right>left:
            v = numbers[left]+numbers[right]
            if v==target:
                return [left+1, right+1]
            elif v>target:
                right -= 1
            else:
                left += 1
                
                