class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.split('/')
        res = []
        for ss in s:
            if ss=='.' or ss=='':continue
            elif ss=='..' and res:res.pop()
            elif ss=='..' and not res:continue
            else:res.append(ss)
        return '/'+'/'.join(res)
so = Solution()
print(so.simplifyPath('/../'))
                