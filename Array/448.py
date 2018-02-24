class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [i for i in range(len(nums)+1)]
        for num in nums:
            res[num]=0
        index = 0
        for i in range(len(res)):
            if res[i]!=0:
                res[index]=res[i]
                index+=1
                
        return res[:index]
        