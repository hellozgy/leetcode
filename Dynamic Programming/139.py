class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict)
        n = len(s)
        k = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for step in range(0, n):
            for i in range(1, n-step+1):
                if s[i-1:i+step] in words:
                    k[i][i+step] = 1
                else:
                    for t in range(0, step):
                        if k[i][i+t]==1 and k[i+t+1][i+step]==1:
                            k[i][i+step]=1
                            break
        return k[1][-1]==1
so = Solution()
print(so.wordBreak('leetcode', ['leet','code']))
                
        
        
        