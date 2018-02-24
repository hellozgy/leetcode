# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        inters = sorted(intervals, key=lambda x:x.start)
        
        res = []
        for i in inters:
            if not res:res.append(i)
            else:
                if i.start>res[-1].end:res.append(i)
                else:
                    res[-1].end = max(res[-1].end, i.end)
        return res
                    