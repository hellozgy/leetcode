#发动态规划
# 超时
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        k = [[0 for _ in range(0, n+1)] for _ in range(0, n+1)]
        for step in range(1, n):
            for i in range(1, n-step+1):
                k[i][i+step]=max(step*min(height[i-1],height[i+step-1]), k[i+1][i+step], k[i][i+step-1])
        return k[1][n]
'''

# 参考答案
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left, right = 0, len(height)-1
        while left<right:
            h = min(height[left], height[right])
            water = max(water, (right-left)*h)
            while height[left]<=h and left<right:left+=1
            while height[right]<=h and left<right:right-=1
        return water
