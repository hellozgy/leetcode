class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 2]
        if n<=2:return res[n-1]
        for i in range(2, n):
            res.append(res[i-1] + res[i-2])
        return res[n-1]
