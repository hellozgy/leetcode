class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        for i in range(len(triangle)):
            if i!=0:
                for j in range(len(triangle[i])):
                    if j==0:triangle[i][j]+=triangle[i-1][0]
                    elif j==i:triangle[i][j]+=triangle[i-1][j-1]
                    else:
                        triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
so =Solution()
print(so.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))