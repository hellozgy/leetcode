class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:return False
        start, end = 0, len(matrix)-1
        while start < end:
            mid = (start+end)//2
            if matrix[mid][0]==target:return True
            elif matrix[mid][0]>target:end = mid-1
            else:
                if matrix[mid][-1]>=target:
                    start, end = mid, mid
                else:
                    start = mid+1
        nums = matrix[start]
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid]==target:return True
            elif nums[mid]>target:end = mid-1
            else:start = mid+1
        return False
        