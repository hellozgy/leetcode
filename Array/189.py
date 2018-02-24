class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp=[]
        k %= len(nums)
        for i in range(k):
            temp.append(nums[len(nums)-k+i])
        for j in range(len(nums)-k-1, -1, -1):
            nums[j+k]=nums[j]
        for i in range(k):
            nums[i]=temp[i]
            
so = Solution()
nums=[1,2,3,4,5,6,7]
so.rotate(nums, 3)
print(nums)