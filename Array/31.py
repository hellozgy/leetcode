class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        tag = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                min_index = self.find_min(nums, i, len(nums) - 1, nums[i - 1])
                self.swap(nums, i - 1, min_index)
                self.sort(nums, i, len(nums) - 1)
                tag = True
                break
        if not tag: nums.reverse()

    def find_min(self, nums, start, end, target):
        min_index = start
        for i in range(start + 1, end + 1, 1):
            if nums[i] > target and nums[i] < nums[min_index]:
                min_index = i
        return min_index

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def sort(self, nums, start, end):
        if start >= end: return
        tag = nums[start]
        left, right = start, end
        index = start
        while index <= right:
            if nums[index] == tag:
                index += 1
            elif nums[index] > tag:
                self.swap(nums, index, right)
                right -= 1
            else:
                self.swap(nums, index, left)
                left += 1
        self.sort(nums, start, left - 1)
        self.sort(nums, right + 1, end)

so = Solution()
d = [1,2,3]
so.nextPermutation(d)
print(d)
d = [3,2,1]
so.nextPermutation(d)
print(d)
d = [1,1,5]
so.nextPermutation(d)
print(d)
d = [1,3,2]
so.nextPermutation(d)
print(d)