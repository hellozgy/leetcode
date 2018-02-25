class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = []
        index = 0
        l = set(['(','{','['])
        while index<len(s):
            c = s[index]
            if c in l:
                m.append(c)
            else:
                if c == ']' and m and m[-1]=='[':
                    m.pop()
                elif c==')' and m and m[-1]=='(':
                    m.pop()
                elif c=='}' and m and m[-1]=='{':
                    m.pop()
                else:
                    return False
            index += 1
        return not m