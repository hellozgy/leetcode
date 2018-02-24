class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        s = str(abs(x))
        p1 = 0
        p2 = len(s)-1
        while p1<p2:
            if s[p1]!=s[p2]:return False
            p1+=1
            p2-=1
        return True