class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        any time the price goes up we want to buy
        """
        total_earnings = 0 

        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                total_earnings += prices[i+1] - prices[i]
        
        return total_earnings
        