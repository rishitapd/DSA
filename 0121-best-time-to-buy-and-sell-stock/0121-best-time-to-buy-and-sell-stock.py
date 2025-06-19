class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_prices=0
        max_profit=0
        for j in range(len(prices)):
            if prices[j]< prices[min_prices] :
                min_prices=j
                j+=1
            elif j>min_prices and prices[j]>prices[min_prices]:
                profit=prices[j]-prices[min_prices]
                max_profit=max(max_profit,profit)
                j+=1
            else:
                j+=1    
        return max_profit
        