class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res = []
        m = set(['+','-','*','/'])
        for token in tokens:
            if token in m:
                b = res.pop()
                a = res.pop()
                if token=='/':
                    tt = a//b
                    tt = tt+1 if (tt<0 and a%b!=0) else tt
                    res.append(tt)
                elif token=='+':
                    res.append(a+b)
                elif token=='-':
                    res.append(a-b)
                else:
                    res.append(a*b)
            else:
                res.append(int(token))
        return res[-1]
so = Solution()
#print(so.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(so.evalRPN(["0","3","/"]))