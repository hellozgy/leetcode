
# 方案一：直接找，每次判断在左边还是右边，（二分查找递归实现）
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.f(nums, 0, len(nums)-1, target)
        
    def f(self, nums, start, end, target):
        if end<start:return -1
        if start==end:return start if nums[start]==target else -1
        mid = (start+end)//2
        if nums[mid]==target:return mid
        if nums[mid]<target:
            if nums[start]<=nums[mid]:
                return self.f(nums, mid+1, end, target)
            else:
                if nums[end]>=target:
                    return self.f(nums, mid+1, end, target)
                else:
                    return self.f(nums, start, mid-1, target)
        else:
            if nums[start]>nums[mid]:
                return self.f(nums, start, mid-1, target)
            else:
                if nums[start]<=target:
                    return self.f(nums, start, mid-1, target)
                else:
                    return self.f(nums, mid+1, end, target)
            
'''

# 方案二：先二分查找到最小值下标，再二分查找（二分查找循环实现）
# 参考答案
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)//2
            if nums[mid]>nums[end]:
                start = mid+1
            else:
                end = mid
        rot = start
        start, end = 0, len(nums)-1
        while start<=end:    
            mid = (start+end)//2
            realmid = (mid+rot)%len(nums)
            if nums[realmid]==target:return realmid
            elif nums[realmid]>target:end = mid-1
            else:start = mid+1
        return -1
                
 
so = Solution()
print(so.search([3,1], 1))       