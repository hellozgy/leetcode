class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1 :return x
        return self.f(0, x, x)
    
    def f(self, start, end, x):
        if start==end :return start
        mid = (start+end)//2
        if mid**2<=x and (mid+1)**2>x:return mid
        elif (mid+1)**2<=x:return self.f(mid+1, end, x)
        else: return self.f(start, mid, x)
so = Solution()
print(so.mySqrt(5))
            