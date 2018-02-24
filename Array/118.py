class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            if i ==0:
                res.append([1])
            else:
                t = []
                tt = res[-1]
                for j in range(len(tt)):
                    if j==0:
                        t=[1]
                    else:
                        t.append(tt[j]+tt[j-1])
                t.append(1)
                res.append(t)              
        return res
so=Solution()
print(so.generate(5))