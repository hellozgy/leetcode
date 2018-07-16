class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return len(s)
        char_index = {}
        max_len = 0
        pre_index = -1
        for i in range(len(s)):
            if s[i] in char_index:
                pre_index = max(pre_index, char_index[s[i]])

            max_len = max(max_len, i - pre_index)
            char_index[s[i]] = i

        return max_len
