class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:return 0
        
        min = nums[-1]
        min_index = len(nums)
        min_tag = True
        
        max = nums[0]
        max_index = -1
        max_tag = True
        
        for i in range(len(nums)):
            ii = len(nums)-1-i
            if nums[ii]<=min:
                if min_tag:
                    min = nums[ii]
                else:
                    min = nums[ii]
                    min_index = ii
                    min_tag = True
            else:
                min_tag = False
                min_index = len(nums)
                
            
            if nums[i]>=max:
                if max_tag:
                    max = nums[i]
                else:
                    max = nums[i]
                    max_tag = True
                    max_index = i
            else:
                max_tag = False
                max_index = -1
        if max_tag: 
            if min_tag:
                
                res = max_index-min_index-1
                return res if res>0 else 0
            else:
                return max_index
        else:
            if min_tag:
                return len(nums)-min_index-1
            else:
                return len(nums)

so = Solution()
print(so.findUnsortedSubarray([1,2,3,4]))
                
            
            