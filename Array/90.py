class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        self.f(nums, res, [])
        return res
    
    def f(self, nums, res, comb):
        if len(nums)==0:
            res.append(comb)
            return
        self.f(nums[1:], res, comb+[nums[0]])
        index = 1
        while index<len(nums) and nums[index]==nums[0]:index+=1
        self.f(nums[index:], res, comb)

class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:return []
        res=[]
        cur=[]
        nums = sorted(nums)
        self.find(nums, 0, res, cur)
        return res

    def find(self, data, index, res, cur):
        if index==len(data):
            res.append(cur)
            return
        end = index
        while end+1<len(data) and data[end+1]==data[index]:end+=1
        for i in range(0, end-index+2):
            self.find(data, end+1, res, cur+[data[index] for _ in range(i)])
so = Solution()
print(so.subsetsWithDup([1,2,2,2,2,2,2,2,2]))