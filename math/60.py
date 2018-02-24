class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        t = [1]
        for i in range(1, n+1):
            t.append(i*t[-1])
        a=[i for i in range(1, n+1)]
        for i in range(1, n+1):
            index = k//t[n-i]
            if k%t[n-i]==0:index-=1
            res.append(str(a[index]))
            a.remove(a[index])
            k %= t[n-i]
        return ''.join(res)

so = Solution()
print(so.getPermutation(4, 3))
            