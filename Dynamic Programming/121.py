class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = []
        minc = float('inf')
        for i in range(len(prices)):
            minc = min(minc,prices[i])
            if i==0:res.append(0)
            else:
                res.append(max(res[i-1], prices[i]-minc))
        return res[-1] if len(res)>0 else 0
