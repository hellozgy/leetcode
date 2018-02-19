class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n<=1:return s
        m_len = 1
        m_res = s[0]
        k = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            k[i][i]=1
        for i in range(1, n):
            k[i][i+1] = 1 if s[i-1]==s[i] else 0
            if k[i][i+1]==1 and m_len<2:
                m_len=2
                m_res=s[i-1:i+1]
        
        for step in range(2, n):
            for i in range(1, n-step+1):
                if k[i+1][i+step-1]==1 and s[i-1]==s[i+step-1]:
                    k[i][i+step] = 1
                    if step+1>m_len:
                        m_len = step + 1
                        m_res = s[i-1:i+step]
        return m_res            
         
solution = Solution()
print(solution.longestPalindrome('cbbd'))
        