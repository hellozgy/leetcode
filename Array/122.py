class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return 0
        profit = 0
        
        low = prices[0]
        i = 1
        while i<len(prices):
            if prices[i]>low:
                high= prices[i]
                index = i
                for j in range(i+1, len(prices)):
                    if prices[j]>=high:
                        index = j
                        high = prices[j]
                    else:
                        break
                
                profit+=high-low
                
                low = high
                i = index
                
            else:
                low = prices[i]
                i+=1
        return profit
so=Solution()
print(so.maxProfit([1,2, 4, 7]))
            
            