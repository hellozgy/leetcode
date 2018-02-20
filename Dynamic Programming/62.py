class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:return 1
        k=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            k[i][0] = 1
        for i in range(n):
            k[0][i] = 1
            
        for mm in range(1, m):
            for nn in range(1, n):
                k[mm][nn] = k[mm-1][nn]+k[mm][nn-1]
        return k[-1][-1]

so = Solution()
print(so.uniquePaths(3, 7))