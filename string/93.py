class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.f(s, 0, [], res)
        return res
    def f(self, s, n, comb, res):
        if n==4:
            if not s:
                res.append('.'.join(comb))
            return
        elif not s:return
        else:
            self.f(s[1:], n+1, comb+[s[0]], res)
            if len(s)>=2 and int(s[:2])>=10:
                self.f(s[2:], n+1, comb+[s[:2]], res)
            if len(s)>=3 and int(s[:3])>=100 and int(s[:3])<=255:
                self.f(s[3:], n+1, comb+[s[:3]], res)
                
so = Solution()
print(so.restoreIpAddresses('25525511135'))                
        
