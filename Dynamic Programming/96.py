class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return 0
        k = [[0 for _ in range(1+n)] for _ in range(1+n)]
        for i in range(1+n):
            k[i][i]=1
        for step in range(1, n):
            for i in range(1, n-step+1):
                k[i][i+step] = self.build(k, i, i+step)
        return k[1][n]
    
    def build(self, k, low, high):
        num = 0
        for i in range(low, high+1):
            l = k[low][i-1] if i>low else 1
            r = k[i+1][high] if high > i else 1
            num += l * r
        return num
so = Solution()
print(so.numTrees(3))