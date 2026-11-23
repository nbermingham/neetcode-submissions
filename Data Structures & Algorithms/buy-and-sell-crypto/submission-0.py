class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        every time there's a local min, keep track of it, and subtract it from the next local max. Compare that to a global max_profit and replace if bigger. Return that max_profit at the end.
        """

        max_profit = 0
        local_min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > local_min:
                max_profit = max(max_profit, prices[i] - local_min)
            else:
                local_min = prices[i]
            
        
        return max_profit