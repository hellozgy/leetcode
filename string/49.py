class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        letter2id = {}
        for char in set(''.join(strs)):
            letter2id[char] = len(letter2id)

        tmp = {}
        for s in strs:
            ss = [0 for _ in range(len(letter2id))]
            for char in s:
                ss[letter2id[char]] += 1
            ss = '_'.join(map(str, ss))
            if ss in tmp:
                tmp[ss].append(s)
            else:
                tmp[ss] = [s]
        return tmp.values()



