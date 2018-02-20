class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or s[0]=='0':return 0
    
        res = [1]
        for i in range(1, len(s)):
            if s[i]=='0':
                if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:
                    res.append(res[i-2] if i-2>=0 else 1)
                else:
                    return 0
            else:
                if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>=11:
                    res.append(res[i-1]+(res[i-2] if i-2>=0 else 1))
                else:
                    res.append(res[i-1])
        return res[-1]
                
so = Solution()
print(so.numDecodings('10'))
                