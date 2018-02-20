class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        res[0][0]=1
        for i in range(1, m):
            if obstacleGrid[i][0]!=1:
                res[i][0]=res[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j]!=1:
                res[0][j]=res[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    res[i][j] = res[i-1][j]+res[i][j-1]
        return res[-1][-1]