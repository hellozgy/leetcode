class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.f(0, n, n, res, '')
        return res
        
        
    def f(self, m, left, right, res, comb):
        if right==0:
            res.append(comb)
            return
        elif left==0:
            res.append(comb+')'*right)
            return
        if m==0:
            self.f(1, left-1, right, res, comb+'(')
        elif m>0:
            self.f(m+1, left-1, right, res, comb+'(')
            self.f(m-1, left, right-1, res, comb+')')
so = Solution()
print(so.generateParenthesis(3))               
            