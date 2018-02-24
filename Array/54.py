class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:return []
        tag = 0# 0右，1下。2左，3上
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []
        while left<=right and top<=bottom:
            if tag==0:
                res.extend(matrix[top][left:right+1])
                top+=1
            elif tag==1: 
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1
            elif tag==2:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom-=1
            elif tag == 3:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
            tag = (tag+1)%4
        return res
                
            